# Generated by Django 4.1.4 on 2023-01-01 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_employer',
            field=models.BooleanField(default=False, verbose_name='کارفرما'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_job_seeker',
            field=models.BooleanField(default=False, verbose_name='کارجو'),
        ),
    ]
