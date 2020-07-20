from django.db import models

# Create your models here.
class Tags(models.Model):
    id=models.IntegerField(primary_key=True)
    tag_name=models.CharField(max_length=20)