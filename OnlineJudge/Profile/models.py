from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from Institution import models as Institution_model
from django.contrib.auth.models import User
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
# Create your models here.


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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    google_id=models.CharField(max_length=100, null=True)
    mobile_no=PhoneNumberField(unique=True,  null=True)
    cur_rating=models.IntegerField(null=True)
    have_profile_image=models.ImageField(upload_to=UploadToPathAndRename(os.path.join('upload','profile_image')), null=True)
    institution_id=models.ForeignKey(Institution_model.Institution, on_delete=models.SET_NULL,  null=True)

    def __str__(self) -> object:
        return '{}'.format(self.user)