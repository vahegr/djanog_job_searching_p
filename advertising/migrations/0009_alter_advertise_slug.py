# Generated by Django 4.1.4 on 2022-12-31 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertising', '0008_alter_advertise_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertise',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, verbose_name='آدرس پست'),
        ),
    ]
