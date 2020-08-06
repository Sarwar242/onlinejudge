from django.db import models
from Profile import models as Profile_model
from Contest import models as Contest_model
from Problem import models as Problem_model

# Create your models here.
class Language(models.Model):
    name=models.CharField(max_length=10)

    
class Submission(models.Model):
    code=models.TextField()
    time_taken=models.DurationField()
    memory_used=models.IntegerField()
    submitted_at=models.DateTimeField(auto_now_add=True)
    verdict=models.CharField(max_length=5)
    language_id=models.ForeignKey(Language, on_delete=models.CASCADE)
    profile_id=models.ForeignKey(Profile_model.Profile, on_delete=models.CASCADE)
    contest_id=models.ForeignKey(Contest_model.Contest, on_delete=models.CASCADE)
    problem_id=models.ForeignKey(Problem_model.Problem, on_delete=models.CASCADE)

    
    def __str__(self) -> object:
        return '{}'.format(self.code)

