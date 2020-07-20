from django.db import models
from User import models as User_models
from Contest import models as Contest_models
from Problem import models as Problem_models

# Create your models here.
class Languages(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=10)
class Submissions(models.Model):
    id=models.IntegerField(primary_key=True)
    code=models.TextField()
    time_taken=models.DurationField()
    memory_used=models.IntegerField()
    submitted_at=models.DateTimeField(auto_now_add=True)
    verdict=models.CharField(max_length=5)
    language_id=models.ForeignKey(Languages, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User_models.Users, on_delete=models.CASCADE)
    contest_id=models.ForeignKey(Contest_models.Contests, on_delete=models.CASCADE)
    problem_id=models.ForeignKey(Problem_models.Problems, on_delete=models.CASCADE)

