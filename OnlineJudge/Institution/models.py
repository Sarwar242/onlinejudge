from django.db import models

# Create your models here.
class Countries(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)

class Institutions(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    country_id=models.ForeignKey(Countries, on_delete=models.CASCADE)