from celery import shared_task
from OnlineJudge.OnlineJudge.celery import app as celery_app # Ensures app is loaded
from Submission.models import Submission, Language
from Problem.models import Problem, Input as ProblemInput
import os
import subprocess
import uuid
import shutil # For cleaning up directories
import datetime # Added for timedelta
import stat # For os.chmod

ISOLATE_PATH = "/usr/bin/isolate"

LANGUAGE_CONFIG = {
    "c++": {
        "source_file": "source.cpp",
        "needs_compilation": True,
        "compile_cmd": ["g++", "-std=c++17", "source.cpp", "-o", "executable"],
        "run_cmd": ["./executable"] # Relative to /box
    },
    "python": {
        "source_file": "source.py",
        "needs_compilation": False,
        "run_cmd": ["python3", "source.py"] # Relative to /box
    },
    # Add other languages here
}

def parse_isolate_meta(meta_file_path):
    """Parses an isolate meta file and returns a dictionary."""
    meta_content = {}
    if os.path.exists(meta_file_path):
        with open(meta_file_path, "r") as f_meta:
            for line in f_meta:
                if ":" in line:
                    key, value = line.strip().split(":", 1)
                    meta_content[key] = value.strip()
    return meta_content

@shared_task(bind=True)
def judge_submission(self, submission_id):
    base_judge_dir = None
    box_path = None
    submission = None

    try:
        submission = Submission.objects.get(pk=submission_id)
        problem = submission.problem_id
        language_obj = submission.language_id

        submission.verdict = "P"
        submission.compile_output = ""
        submission.time_taken = datetime.timedelta(seconds=0)
        submission.memory_used = 0
        submission.save()

        lang_key = language_obj.name.lower()
        lang_config = LANGUAGE_CONFIG.get(lang_key)

        if not lang_config:
            submission.verdict = "LANGE"
            submission.compile_output = f"Language '{language_obj.name}' not supported."
            submission.save()
            return f"Language {language_obj.name} not supported for submission {submission_id}."

        judge_run_id = str(uuid.uuid4())
        base_judge_dir = os.path.join("/tmp/judge_runs", judge_run_id)
        os.makedirs(base_judge_dir, exist_ok=True)

        box_path = os.path.join(base_judge_dir, "box")

        init_cmd = [ISOLATE_PATH, f"--box-id={0}", f"--dir={box_path}", "--cg", "--init"]
        init_result = subprocess.run(init_cmd, check=False, capture_output=True, text=True)
        if init_result.returncode != 0:
            error_message = init_result.stderr if init_result.stderr else init_result.stdout
            print(f"Isolate init failed: {error_message}")
            submission.verdict = "JE"
            submission.compile_output = f"Isolate init failed: {error_message}"
            submission.save()
            raise Exception(f"Isolate init failed for submission {submission_id}")

        source_file_on_host = os.path.join(box_path, lang_config["source_file"])
        with open(source_file_on_host, "w") as f:
            f.write(submission.code)

        if lang_config["needs_compilation"]:
            compile_meta_path_on_host = os.path.join(base_judge_dir, "compile.meta")
            processed_compile_cmd = []
            for part in lang_config["compile_cmd"]:
                if part == lang_config["source_file"] or part == "executable":
                    processed_compile_cmd.append(part)
                else:
                    processed_compile_cmd.append(part)

            compile_isolate_cmd = [
                ISOLATE_PATH, f"--box-id={0}", f"--dir={box_path}", "--cg",
                "--processes=128", "--wall-clock=30s", "--time=20s", "--mem=256000",
                f"--meta={compile_meta_path_on_host}",
                "--stdout=_compile.out", "--stderr=_compile.err",
                "--run", "--", *processed_compile_cmd
            ]
            subprocess.run(compile_isolate_cmd, capture_output=True, text=True)
            compile_meta_content = parse_isolate_meta(compile_meta_path_on_host)
            # ... (rest of compile output handling as before) ...
            compile_stdout = ""
            compile_stderr = ""
            stdout_path_in_box_on_host = os.path.join(box_path, "_compile.out")
            stderr_path_in_box_on_host = os.path.join(box_path, "_compile.err")
            if os.path.exists(stdout_path_in_box_on_host):
                with open(stdout_path_in_box_on_host, "r") as f_stdout:
                    compile_stdout = f_stdout.read()
            if os.path.exists(stderr_path_in_box_on_host):
                with open(stderr_path_in_box_on_host, "r") as f_stderr:
                    compile_stderr = f_stderr.read()
            submission.compile_output = f"Compile STDOUT:\n{compile_stdout}\n\nCompile STDERR:\n{compile_stderr}\n\nMeta:\n{compile_meta_content}"
            meta_status = compile_meta_content.get("status")
            exit_code_str = compile_meta_content.get("exitcode", "-1")
            exit_code = -1
            if exit_code_str.isdigit() or (exit_code_str.startswith('-') and exit_code_str[1:].isdigit()):
                 exit_code = int(exit_code_str)
            if meta_status != "EX" or exit_code != 0:
                submission.verdict = "CE"
                submission.save()
                raise Exception(f"Compilation failed. Meta: {compile_meta_content}")

        submission.verdict = "R"
        submission.save()

        overall_verdict = "AC"
        max_time_taken_ms = 0.0
        max_memory_kb = 0
        test_cases = ProblemInput.objects.filter(problem_id=problem).order_by('id')

        if not test_cases.exists():
            overall_verdict = "JE"
            submission.compile_output = (submission.compile_output or "") + "\nNo test cases found for the problem."

        for test_case in test_cases:
            if overall_verdict not in ["AC", "R"]: # If already failed, skip more test cases
                 break

            input_file_on_host = os.path.join(box_path, "input.txt")
            with open(input_file_on_host, "w") as f:
                f.write(test_case.input)

            run_meta_path_on_host = os.path.join(base_judge_dir, f"run_{test_case.id}.meta")
            processed_run_cmd = []
            for part in lang_config["run_cmd"]: # Ensure paths are relative to /box
                if part.startswith("./") or lang_config["source_file"] in part:
                    processed_run_cmd.append(part)
                else:
                    processed_run_cmd.append(part)

            run_isolate_cmd = [
                ISOLATE_PATH, f"--box-id={0}", f"--dir={box_path}", "--cg",
                "--processes",
                f"--wall-clock={int(problem.max_runtime.total_seconds() * 2 + 2)}s", # Generous wall, ensure > time + buffer
                f"--time={problem.max_runtime.total_seconds()}s",
                f"--fsize={1024*1024}", # Limit output file size (e.g. 1MB)
                f"--mem={problem.max_memory}",
                f"--meta={run_meta_path_on_host}",
                "--stdin=input.txt", "--stdout=_run.out", "--stderr=_run.err",
                "--share-net=off", "--run", "--", *processed_run_cmd
            ]
            subprocess.run(run_isolate_cmd, capture_output=True, text=True)
            run_meta = parse_isolate_meta(run_meta_path_on_host)

            current_time_ms = float(run_meta.get("time", 0)) * 1000
            current_memory_kb = int(run_meta.get("max-rss", 0))
            max_time_taken_ms = max(max_time_taken_ms, current_time_ms)
            max_memory_kb = max(max_memory_kb, current_memory_kb)

            run_status = run_meta.get("status")
            run_exit_code_str = run_meta.get("exitcode", "0")
            run_exit_code = 0
            if run_exit_code_str.isdigit() or (run_exit_code_str.startswith('-') and run_exit_code_str[1:].isdigit()):
                 run_exit_code = int(run_exit_code_str)

            if run_status == "TO": overall_verdict = "TLE"; break
            if run_status == "SG": overall_verdict = "RE"; break # Signal implies runtime error
            if run_status == "RE" and run_exit_code !=0 : overall_verdict = "RE"; break # Isolate specific runtime error (e.g. forbidden syscall)
            if run_status == "XX": overall_verdict = "MLE"; break # Isolate killed for resource violation (often memory with --mem)
            if run_status == "EX" and run_exit_code != 0: overall_verdict = "RE"; break
            if current_memory_kb > problem.max_memory: overall_verdict = "MLE"; break

            # Custom Validator Logic or Standard Comparison
            program_output_path_on_host = os.path.join(box_path, "_run.out")
            program_output = ""
            if os.path.exists(program_output_path_on_host):
                with open(program_output_path_on_host, "r") as f_out:
                    program_output = f_out.read()

            if problem.output_validator and problem.output_validator.name:
                validator_script_system_path = problem.output_validator.path
                validator_script_box_name = "validator_script" # Fixed name in box
                validator_script_in_box_on_host = os.path.join(box_path, validator_script_box_name)

                shutil.copy(validator_script_system_path, validator_script_in_box_on_host)
                os.chmod(validator_script_in_box_on_host, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH) # rwxr-xr-x

                expected_output_on_host = os.path.join(box_path, "expected.txt")
                with open(expected_output_on_host, "w") as f_exp:
                    f_exp.write(test_case.expected_output)

                validator_meta_path_on_host = os.path.join(base_judge_dir, f"validator_{test_case.id}.meta")
                validator_isolate_cmd = [
                    ISOLATE_PATH, f"--box-id={0}", f"--dir={box_path}", "--cg",
                    "--processes=64", "--wall-clock=10s", "--time=5s", "--mem=128000",
                    f"--meta={validator_meta_path_on_host}",
                    # Validator gets: user_input.txt, user_output.txt, expected_output.txt
                    # These are paths *inside the box*
                    "--run", "--", f"./{validator_script_box_name}", "input.txt", "_run.out", "expected.txt"
                ]
                subprocess.run(validator_isolate_cmd, capture_output=True, text=True)
                validator_meta = parse_isolate_meta(validator_meta_path_on_host)

                val_status = validator_meta.get("status")
                val_exit_code_str = validator_meta.get("exitcode", "1") # Default to 1 (WA) if no exit code
                val_exit_code = 1 # Default to WA
                if val_exit_code_str.isdigit() or (val_exit_code_str.startswith('-') and val_exit_code_str[1:].isdigit()):
                    val_exit_code = int(val_exit_code_str)

                if val_status != "EX": # Validator itself crashed (TLE, MLE, RE)
                    overall_verdict = "JE"
                    submission.compile_output = (submission.compile_output or "") + f"\nValidator error on TC {test_case.id}: Status {val_status}, Meta: {validator_meta}"
                    break
                if val_exit_code != 0: # Validator judged as Wrong Answer
                    overall_verdict = "WA"
                    break
                # If validator exits 0, it's AC for this test case. Loop continues.
            else:
                # Standard comparison if no validator
                expected_lines = [line.strip() for line in test_case.expected_output.strip().splitlines()]
                program_lines = [line.strip() for line in program_output.strip().splitlines()]
                if expected_lines != program_lines:
                    overall_verdict = "WA"
                    break

        submission.verdict = overall_verdict
        submission.time_taken = datetime.timedelta(milliseconds=max_time_taken_ms)
        submission.memory_used = max_memory_kb
        submission.save()

    except Submission.DoesNotExist:
        print(f"Submission with id {submission_id} not found.")
    except Exception as e:
        print(f"An error occurred during judging submission {submission_id}: {e}")
        if submission:
            submission.verdict = "JE"
            submission.compile_output = (submission.compile_output or "") + f"\nError: {type(e).__name__}: {str(e)}"
            submission.save()
    finally:
        if box_path and os.path.exists(box_path):
            cleanup_cmd = [ISOLATE_PATH, f"--box-id={0}", f"--dir={box_path}", "--cg", "--cleanup"]
            subprocess.run(cleanup_cmd, check=False, capture_output=True, text=True)
        if base_judge_dir and os.path.exists(base_judge_dir):
            shutil.rmtree(base_judge_dir)

    if submission:
        return f"Judging complete for submission {submission_id}. Verdict: {submission.verdict}"
    else:
        return f"Judging process had an issue for submission {submission_id}, submission object might not be available."

# Example of how to call this task:
# from .tasks import judge_submission
# judge_submission.delay(submission_id=some_submission.id)
