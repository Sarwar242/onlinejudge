from django.db import models

# Create your models here.
class Language(models.Model):
    name=models.CharField(max_length=10)

    
class Submission(models.Model):
    code=models.TextField()
    time_taken=models.DurationField()
    memory_used=models.IntegerField()
    submitted_at=models.DateTimeField(auto_now_add=True)
    verdict=models.CharField(max_length=5)
    compile_output = models.TextField(blank=True, null=True)
    language_id=models.ForeignKey(Language, on_delete=models.CASCADE)
    profile_id=models.ForeignKey('Profile.Profile', on_delete=models.CASCADE)
    contest_id=models.ForeignKey('Contest.Contest', on_delete=models.CASCADE)
    problem_id=models.ForeignKey('Problem.Problem', on_delete=models.CASCADE)

    
    def __str__(self) -> object:
        return '{}'.format(self.code)

