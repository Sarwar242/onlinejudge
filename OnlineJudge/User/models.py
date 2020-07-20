from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from Institution import models as Institution_models
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

@deconstructible
class UploadToPathAndRename(object):
    def __init__(self, path):
        self.sub_path=path
    def __call__(self, instance, filename):
        ext=filename.split('.')[-1]
        if instance.pk:
            filename='{}.{}'.format(instance.pk, ext)
        else:
            filename='{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.sub_path, filename)
class Users(models.Model):
    id=models.IntegerField(primary_key=True)
    google_id=models.CharField(max_length=100)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    username=models.CharField(unique=True, max_length=20)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    mobile_no=PhoneNumberField(unique=True)
    cur_rating=models.IntegerField()
    have_profile_image=models.ImageField(upload_to=UploadToPathAndRename(os.path.join('upload','profile_image')))
    institution_id=models.ForeignKey(Institution_models.Institutions, on_delete=models.CASCADE)