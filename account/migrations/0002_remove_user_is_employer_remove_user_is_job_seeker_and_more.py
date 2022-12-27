# Generated by Django 4.1.4 on 2022-12-26 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_employer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_job_seeker',
        ),
        migrations.AddField(
            model_name='user',
            name='type_of_user',
            field=models.CharField(choices=[('1', 'کارجو'), ('2', 'کارفرما')], default='1', max_length=1, verbose_name='نوع کاربر'),
        ),
    ]
