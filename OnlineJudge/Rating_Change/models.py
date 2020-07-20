from django.db import models
from Contest import models as Contest_models
from User import models as User_models

# Create your models here.
class Rating_Change(models.Model):
    contest_id=models.ForeignKey(Contest_models.Contests, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User_models.Users, on_delete=models.CASCADE)
    rating_change=models.IntegerField()

    class Meta:
        unique_together = (("contest_id", "user_id"),)