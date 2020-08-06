from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_name=models.CharField(max_length=20)
    
    def __str__(self) -> object:
        return '{}'.format(self.tag_name)