# Generated by Django 2.0.1 on 2018-01-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_task_my_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='content',
            new_name='content_1',
        ),
        migrations.AddField(
            model_name='task',
            name='content_2',
            field=models.TextField(default='example'),
            preserve_default=False,
        ),
    ]
