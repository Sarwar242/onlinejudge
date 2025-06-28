from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Rating_Status(models.Model):
    min_rating=models.IntegerField()
    status=models.CharField(max_length=30)
    color=ColorField(default='#FF0000')
        
    def __str__(self) -> object:
        return '{}'.format(self.status)
    class Meta:
        verbose_name = "Rating Status"
        verbose_name_plural = "Rating Status"


class Rating_Change(models.Model):
    contest_id=models.ForeignKey('Contest.Contest', on_delete=models.CASCADE)
    profile_id=models.ForeignKey('Profile.Profile', on_delete=models.CASCADE)
    rating_change=models.IntegerField()

    def __str__(self) -> object:
        return '{}'.format(self.profile_id.name)

    class Meta:
        unique_together = (("contest_id", "profile_id"),)
        verbose_name = "Rating Change"
        verbose_name_plural = "Rating Changes"