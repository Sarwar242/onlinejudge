from django.db import models
from Profile import models as Profile_model

# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self) -> object:
        return '{}'.format(self.name)

class Team_Member(models.Model):
    team_id=models.ForeignKey(Team, on_delete=models.CASCADE)
    profile_id=models.ForeignKey(Profile_model.Profile, on_delete=models.CASCADE)

    def __str__(self) -> object:
        return '{}'.format(self.team_id.name)
    
    class Meta:
        unique_together = (("team_id", "profile_id"),)
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
