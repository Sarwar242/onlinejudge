from django.db import models
from User import models as User_models

# Create your models here.
class Teams(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)

class Team_Members(models.Model):
    team_id=models.ForeignKey(Teams, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User_models.Users, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (("team_id", "user_id"),)
