# Generated by Django 3.1 on 2020-08-18 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Problem', '0001_initial'),
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ask_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField(blank=True)),
                ('is_public', models.BooleanField(default=False)),
                ('contest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contest.contest')),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.profile')),
            ],
            options={
                'verbose_name': 'Ask Question',
                'verbose_name_plural': 'Ask Questions',
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('contest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contest.contest')),
            ],
        ),
        migrations.CreateModel(
            name='Conetest_Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contest.contest')),
                ('problem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Problem.problem')),
            ],
            options={
                'verbose_name': 'Conntest Problem',
                'verbose_name_plural': 'Contest Problems',
                'unique_together': {('contest_id', 'problem_id')},
            },
        ),
    ]
