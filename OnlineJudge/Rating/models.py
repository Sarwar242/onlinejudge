from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Rating_Statuses(models.Model):
    id=models.IntegerField(primary_key=True)
    min_rating=models.IntegerField()
    status=models.CharField(max_length=30)
    color=ColorField(default='#FF0000')