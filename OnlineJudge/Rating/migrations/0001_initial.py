# Generated by Django 3.1 on 2020-08-18 11:27

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Contest', '0001_initial'),
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_rating', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
            ],
            options={
                'verbose_name': 'Rating Status',
                'verbose_name_plural': 'Rating Status',
            },
        ),
        migrations.CreateModel(
            name='Rating_Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_change', models.IntegerField()),
                ('contest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contest.contest')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.profile')),
            ],
            options={
                'verbose_name': 'Rating Change',
                'verbose_name_plural': 'Rating Changes',
                'unique_together': {('contest_id', 'profile_id')},
            },
        ),
    ]
