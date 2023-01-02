# Generated by Django 4.1.4 on 2022-12-31 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='آدرس ایمیل')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='نام کاربری')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='نام و نام خانوادگی')),
                ('phone', models.CharField(blank=True, max_length=12, null=True, unique=True, verbose_name='شماره مبایل')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/users', verbose_name='تصویر کاربر')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='درباره')),
                ('skill', models.CharField(max_length=150, verbose_name='حرفه')),
                ('status', models.CharField(choices=[('1', 'مجرد'), ('2', 'متاهل')], default='1', max_length=1, verbose_name=' تاهل')),
                ('education', models.CharField(max_length=100, verbose_name='مقطع تحصیلی')),
                ('university', models.CharField(max_length=100, verbose_name='نام دانشگاه')),
                ('field', models.CharField(max_length=100, verbose_name='رشته تحصیلی')),
                ('english', models.CharField(max_length=100, verbose_name='میزان تسلط شما به زبان انگلیسی')),
                ('language', models.CharField(max_length=100, verbose_name='آیا به زبان دیگری تسلط دارید؟')),
                ('project', models.CharField(max_length=100, verbose_name='پروژه های کاری')),
                ('certificate', models.CharField(max_length=200, null=True, verbose_name='گواهی نامه ها و افتخارات')),
                ('courses', models.CharField(max_length=100, verbose_name='دوره ها')),
                ('job', models.CharField(max_length=100, verbose_name='تجربه شغلی')),
                ('last_job_situation', models.CharField(max_length=100, verbose_name='آخرین موقعیت شغلی')),
                ('city', models.CharField(max_length=100, verbose_name='شهر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعالیت')),
                ('is_admin', models.BooleanField(default=False, verbose_name='ادمین')),
                ('type_of_user', models.CharField(choices=[('1', 'کارجو'), ('2', 'کارفرما')], default='1', max_length=1, verbose_name='نوع کاربر')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربر ها',
            },
        ),
    ]
