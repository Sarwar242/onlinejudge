from django.conf import settings
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
        self.sub_path = path
               
    def __call__(self, instance, filename):
        ext=filename.split('.')[-1]
        filename='{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.sub_path, filename)


class profileQuerySet(models.QuerySet):
    pass

class profileManager(models.Manager):
    def get_queryset(self):
        return profileQuerySet(self.model, using=self._db)

class Profile(models.Model):
    user =models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    google_id=models.CharField(max_length=100, null=True, blank=True)
    mobile_no=PhoneNumberField(unique=True,  null=True)
    cur_rating=models.IntegerField(default=0,null=True)
    have_profile_image=models.ImageField(upload_to=UploadToPathAndRename(os.path.join('upload','profile_image')), null=True)
    institution_id=models.ForeignKey(Institution_model.Institution, on_delete=models.SET_NULL,  null=True)

    def __str__(self) -> object:
        return '{}'.format(self.user)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'