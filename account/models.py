from django.db import models
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    TYPE_CHOICE = (
        ('1', 'کارجو'),
        ('2', 'کارفرما'),
    )
    MARITAL_SITUATION = (
        ('1', 'مجرد'),
        ('2', 'متاهل'),)
    email = models.EmailField(
        verbose_name='آدرس ایمیل',
        max_length=255,
        unique=True,)
    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='نام کاربری')
    full_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='نام و نام خانوادگی')
    phone = models.CharField(
        max_length=12,
        unique=True,
        blank=True,
        null=True,
        verbose_name='شماره مبایل')
    image = models.ImageField(
        upload_to='images/users',
        null=True,
        blank=True,
        verbose_name='تصویر کاربر')
    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name='درباره')
    skill = models.CharField(
        max_length=150,
        null=True,
        verbose_name="حرفه")
    status = models.CharField(
        max_length=1,
        choices=MARITAL_SITUATION,
        default='1',
        verbose_name=" تاهل")
    education = models.CharField(
        max_length=100,
        verbose_name="مقطع تحصیلی")
    university = models.CharField(
        max_length=100,
        verbose_name="نام دانشگاه")
    field = models.CharField(
        max_length=100,
        verbose_name="رشته تحصیلی")
    english = models.CharField(
        max_length=100,
        verbose_name="میزان تسلط شما به زبان انگلیسی")
    language = models.CharField(
        max_length=100,
        verbose_name="آیا به زبان دیگری تسلط دارید؟")
    project = models.CharField(
        max_length=100,
        verbose_name="پروژه های کاری")
    certificate = models.CharField(
        max_length=200,
        verbose_name="گواهی نامه ها و افتخارات",
        null=True)
    courses = models.CharField(
        max_length=100,
        verbose_name="دوره ها")
    job = models.CharField(
        max_length=100,
        verbose_name="تجربه شغلی")
    last_job_situation = models.CharField(
        max_length=100,
        verbose_name="آخرین موقعیت شغلی")
    city = models.CharField(
        max_length=100,
        verbose_name="شهر")
    is_active = models.BooleanField(
        default=True,
        verbose_name='فعالیت')
    is_admin = models.BooleanField(
        default=False,
        verbose_name='ادمین')
    type_of_user = models.CharField(
        max_length=1,
        choices=TYPE_CHOICE,
        default='1',
        verbose_name="نوع کاربر")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر ها'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        " Is the user a member of staff? "
        # Simplest possible answer: All admins are staff
        return self.is_admin
