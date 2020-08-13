from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self) -> object:
        return '{}'.format(self.name)
    
    class Meta:
        verbose_name_plural = "Countries"

class Institution(models.Model):
    name=models.CharField(max_length=100)
    country_id=models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self) -> object:
        return '{}'.format(self.name)