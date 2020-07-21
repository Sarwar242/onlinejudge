from django.db import models
from django.core.validators import RegexValidator
from Tag import models as Tag_models
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
#FileField(upload_to=path_and_rename('output_validator/'),)
class Problems(models.Model):
    problem_id=models.IntegerField(primary_key=True)
    url_ext=models.CharField(
        max_length=10, 
        validators=[RegexValidator('^[A-Z]*$','Only uppercase letters allowed.')],
    )
    name=models.CharField(max_length=50)
    description=models.TextField()
    output_producer=models.FileField(upload_to=UploadToPathAndRename(os.path.join('upload','output_producer')))
    output_validator=models.FileField(upload_to=UploadToPathAndRename(os.path.join('upload','output_validator')))
    explanations=models.TextField()
    difficulty=models.IntegerField()
    max_runtime=models.DurationField()
    max_memory=models.IntegerField()

class Problem_Tags(models.Model):
    problem_id=models.ForeignKey(Problems, on_delete=models.CASCADE)
    tag_id=models.ForeignKey(Tag_models.Tags, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("problem_id", "tag_id"),)

class Inputs(models.Model):
    input_id=models.IntegerField(primary_key=True)
    input=models.TextField()
    is_simple=models.BooleanField(default=True)
    problem_id=models.ForeignKey(Problems, on_delete=models.CASCADE)

