from django.db import models
from django.core.validators import RegexValidator
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
class Problem(models.Model):
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

    def __str__(self) -> object:
        return '{}'.format(self.name)


class Problem_Tag(models.Model):
    problem_id=models.ForeignKey(Problem, on_delete=models.CASCADE)
    tag_id=models.ForeignKey('Tag.Tag', on_delete=models.CASCADE)
    def __str__(self) -> object:
        return '{}'.format(self.problem_id.name)

    class Meta:
        unique_together = (("problem_id", "tag_id"),)
        verbose_name = "Problem Tag"
        verbose_name_plural = "Problem Tags"

class Input(models.Model):
    input=models.TextField()
    expected_output = models.TextField(default='')
    is_simple=models.BooleanField(default=True)
    problem_id=models.ForeignKey(Problem, on_delete=models.CASCADE)
    def __str__(self) -> object:
        return '{}'.format(self.input)



