from django.db import models
from Problem import models as Problem_model
from Profile import models as Profile


# Create your models here.
class Contest(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    start_at=models.DateTimeField()
    end_at=models.DateTimeField()

    def __str__(self) -> object:
        return '{}'.format(self.name)
        

class Conetest_Problem(models.Model):
    contest_id=models.ForeignKey(Contest, on_delete=models.CASCADE)
    problem_id=models.ForeignKey(Problem_model.Problem, on_delete=models.CASCADE)
    def __str__(self) -> object:
        return '{}'.format(self.contest_id.name)

    class Meta:
        unique_together = (("contest_id", "problem_id"),)

class Announcement(models.Model):
    contest_id=models.ForeignKey(Contest, on_delete=models.CASCADE)
    description=models.TextField()
    def __str__(self) -> object:
        return '{}'.format(self.contest_id.name)

class Ask_Question(models.Model):
    contest_id=models.ForeignKey(Contest, on_delete=models.CASCADE)
    profile_id=models.ForeignKey(Profile.Profile, on_delete=models.CASCADE)
    question=models.TextField()
    answer=models.TextField(blank=True)
    is_public=models.BooleanField(default=False)
    def __str__(self) -> object:
        return '{}'.format(self.question)
