from django.db import models
from django.utils import timezone
from account.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="ادرس اینترنتی")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته"
        verbose_name_plural = "دسته ها"


class Advertise(models.Model):
    STATUS_CHOICE = (
        ('p', 'published'),
        ('d', 'draft'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='منتشر کننده')
    title = models.CharField(max_length=150, verbose_name="موضوع")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس پست")
    category = models.ManyToManyField(Category, verbose_name="موقعیت شغلی", related_name="advertise")
    name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=11, verbose_name="شماره تماس")
    email = models.EmailField(max_length=100, verbose_name="ایمیل")
    company = models.CharField(max_length=100, verbose_name="نام شرکت")
    city = models.CharField(max_length=100, verbose_name="شهر")
    description = models.TextField(max_length=9000, verbose_name="متن آگهی")
    thumbnail = models.ImageField(upload_to="images", verbose_name="آپلود عکس")
    create = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار آگهی")
    publish = models.DateTimeField(default=timezone.now, verbose_name="تاریخ")
    update = models.DateTimeField(auto_now=timezone.now, verbose_name="بروزرسانی پست")
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='p', verbose_name="وضعیت")

    def check_status(self):
        now = timezone.now()
        end_day = self.publish.day + 15
        if now > end_day:
            self.status = 'd'
            self.save()
        return self.status

    def get_absolute_url(self):
        return reverse('home:ad_detail', args=[self.id, self.slug])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "آگهی"
        verbose_name_plural = "آگهی ها"
        ordering = ('-create',)


class Resume(models.Model):
    MARITAL_CHOICE = (
        ('t', 'متاهل'),
        ('j', 'مجرد'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر")
    name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    skill = models.CharField(max_length=150, verbose_name="حرفه")
    status = models.CharField(max_length=1, choices=MARITAL_CHOICE, default='Z', verbose_name=" تاهل")
    education = models.CharField(max_length=100, verbose_name="مقطع تحصیلی")
    university = models.CharField(max_length=100, verbose_name="نام دانشگاه")
    field = models.CharField(max_length=100, verbose_name="رشته تحصیلی")
    english = models.CharField(max_length=100, verbose_name="میزان تسلط شما به زبان انگلیسی")
    language = models.CharField(max_length=100, verbose_name="آیا به زبان دیگری تسلط دارید؟")
    project = models.CharField(max_length=100, verbose_name="پروژه های کاری")
    certificate = models.CharField(max_length=100, verbose_name="گواهی نامه ها و افتخارات")
    dore = models.CharField(max_length=100, verbose_name="دوره ها")
    job = models.CharField(max_length=100, verbose_name="تجربه شغلی")
    last_job_situation = models.CharField(max_length=100, verbose_name="آخرین موقعیت شغلی")
    city = models.CharField(max_length=100, verbose_name="شهر")

    class Meta:
        verbose_name = "رزومه"
        verbose_name_plural = "رزومه ها"

    def __str__(self):
        return self.user.username
