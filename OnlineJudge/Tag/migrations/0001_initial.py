# Generated by Django 3.0.8 on 2020-07-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=20)),
            ],
        ),
    ]