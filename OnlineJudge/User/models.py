from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from Institution import models as Institution_models
import os
from uuid import uuid4

def path_and_rename(path):
    def wrapper(instance,filename):
        ext=filename.split('.')[-1]
        if instance.pk:
            filename='{}.{}'.format(instance.pk,ext)
        else:
            filename='{}.{}'.format(uuid4().hex,ext)
        return os.path.join(path, filename)
    return wrapper
class Users(models.Model):
    id=models.IntegerField(primary_key=True)
    google_id=models.CharField(max_length=100)
    first_name=models.CharField(max_length=30)
    lase_name=models.CharField(max_length=30)
    username=models.CharField(unique=True, max_len=20)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    mobile_no=PhoneNumberField(unique=True)
    cur_rating=models.IntegerField()
    have_profile_image=models.ImageField(upload_to=path_and_rename('profile_image/'))
    institution_id=models.ForeignKey(Institution_models.Institutions, on_delete=models.CASCADE)