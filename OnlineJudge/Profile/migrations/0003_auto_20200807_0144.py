# Generated by Django 3.0.8 on 2020-08-06 19:44

import Profile.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Institution', '0001_initial'),
        ('Profile', '0002_auto_20200807_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cur_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='google_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='have_profile_image',
            field=models.ImageField(null=True, upload_to=Profile.models.UploadToPathAndRename('upload\\profile_image')),
        ),
        migrations.AlterField(
            model_name='profile',
            name='institution_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Institution.Institution'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True),
        ),
    ]