# Generated by Django 3.0.8 on 2020-07-20 17:50

import Problem.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('problem_id', models.IntegerField(primary_key=True, serialize=False)),
                ('url_ext', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[A-Z]*$', 'Only uppercase letters allowed.')])),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('output_producer', models.FileField(upload_to=Problem.models.UploadToPathAndRename('upload\\output_producer'))),
                ('output_validator', models.FileField(upload_to=Problem.models.UploadToPathAndRename('upload\\output_validator'))),
                ('explanations', models.TextField()),
                ('difficulty', models.IntegerField()),
                ('max_runtime', models.DurationField()),
                ('max_memory', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inputs',
            fields=[
                ('input_id', models.IntegerField(primary_key=True, serialize=False)),
                ('input', models.TextField()),
                ('is_simple', models.BooleanField(default=True)),
                ('problem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Problem.Problems')),
            ],
        ),
        migrations.CreateModel(
            name='Problem_Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Problem.Problems')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tag.Tags')),
            ],
            options={
                'unique_together': {('problem_id', 'tag_id')},
            },
        ),
    ]