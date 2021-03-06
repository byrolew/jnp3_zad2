# Generated by Django 2.0.1 on 2018-01-22 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180122_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='tasks',
        ),
        migrations.RemoveField(
            model_name='taskrandom',
            name='P',
        ),
        migrations.RemoveField(
            model_name='taskrandom',
            name='Q',
        ),
        migrations.RemoveField(
            model_name='taskrandom',
            name='content',
        ),
        migrations.RemoveField(
            model_name='taskrandom',
            name='instruction',
        ),
        migrations.RemoveField(
            model_name='taskrandom',
            name='nP',
        ),
        migrations.RemoveField(
            model_name='taskrandom',
            name='nQ',
        ),
        migrations.RemoveField(
            model_name='taskrandom',
            name='rule',
        ),
        migrations.AddField(
            model_name='taskrandom',
            name='task',
            field=models.ForeignKey(default=None, on_delete=False, to='core.Task'),
            preserve_default=False,
        ),
    ]
