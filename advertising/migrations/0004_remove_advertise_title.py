# Generated by Django 4.1.4 on 2022-12-27 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertising', '0003_rename_user_resume_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertise',
            name='title',
        ),
    ]
