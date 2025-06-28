from django.db import models

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
    problem_id=models.ForeignKey('Problem.Problem', on_delete=models.CASCADE)
    def __str__(self) -> object:
        return '{}'.format(self.contest_id.name)

    class Meta:
        unique_together = (("contest_id", "problem_id"),)
        verbose_name = "Conntest Problem"
        verbose_name_plural = "Contest Problems"

class Announcement(models.Model):
    contest_id=models.ForeignKey(Contest, on_delete=models.CASCADE)
    description=models.TextField()
    def __str__(self) -> object:
        return '{}'.format(self.contest_id.name)

class Ask_Question(models.Model):
    contest_id=models.ForeignKey(Contest, on_delete=models.CASCADE)
    profile_id=models.ForeignKey('Profile.Profile', on_delete=models.CASCADE)
    question=models.TextField()
    answer=models.TextField(blank=True)
    is_public=models.BooleanField(default=False)
    def __str__(self) -> object:
        return '{}'.format(self.question)
    class Meta:
        verbose_name = "Ask Question"
        verbose_name_plural = "Ask Questions"
