# Generated by Django 2.0.2 on 2018-09-07 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20180831_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_shorten',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]
