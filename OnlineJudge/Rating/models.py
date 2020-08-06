from django.db import models
from colorfield.fields import ColorField
from Contest import models as Contest_model
from Profile import models as Profile_model

# Create your models here.
class Rating_Status(models.Model):
    min_rating=models.IntegerField()
    status=models.CharField(max_length=30)
    color=ColorField(default='#FF0000')
        
    def __str__(self) -> object:
        return '{}'.format(self.status)


class Rating_Change(models.Model):
    contest_id=models.ForeignKey(Contest_model.Contest, on_delete=models.CASCADE)
    profile_id=models.ForeignKey(Profile_model.Profile, on_delete=models.CASCADE)
    rating_change=models.IntegerField()

    def __str__(self) -> object:
        return '{}'.format(self.profile_id.name)

    class Meta:
        unique_together = (("contest_id", "profile_id"),)