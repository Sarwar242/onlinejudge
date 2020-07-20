from django.db import models
from Problem import models as Problem_models
from User import models as User_models


# Create your models here.
class Contests(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField()
    start_at=models.DateTimeField()
    end_at=models.DateTimeField()

class Conetest_Problems(models.Model):
    contest_id=models.ForeignKey(Contests, on_delete=models.CASCADE)
    problem_id=models.ForeignKey(Problem_models.Problems, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("contest_id", "problem_id"),)

class Announcements(models.Model):
    id=models.IntegerField(primary_key=True)
    contest_id=models.ForeignKey(Contests, on_delete=models.CASCADE)
    description=models.TextField()

class Ask_Questions(models.Model):
    id=models.IntegerField(primary_key=True)
    contest_id=models.ForeignKey(Contests, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User_models.Users, on_delete=models.CASCADE)
    question=models.TextField()
    answer=models.TextField(blank=True)
    is_public=models.BooleanField(default=False)
