# Generated by Django 2.1 on 2018-08-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/orig')),
                ('project_title', models.CharField(max_length=200)),
                ('project_text', models.TextField()),
                ('project_date', models.DateField(verbose_name='Date Finished')),
                ('project_member', models.TextField(default='No one')),
                ('project_extra', models.TextField(default=' ')),
            ],
        ),
    ]
