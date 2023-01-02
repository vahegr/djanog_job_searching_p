from django.db import models
from django.utils import timezone
from django.utils.text import slugify

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
    slug = models.SlugField(max_length=100, verbose_name="آدرس پست", blank=True)
    category = models.ManyToManyField(Category, verbose_name="موقعیت شغلی", related_name="advertise")
    name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=11, verbose_name="شماره تماس")
    email = models.EmailField(max_length=100, verbose_name="ایمیل")
    company = models.CharField(max_length=100, verbose_name="نام شرکت")
    city = models.CharField(max_length=100, verbose_name="شهر")
    description = models.TextField(max_length=9000, verbose_name="متن آگهی")
    thumbnail = models.ImageField(upload_to="images", verbose_name="آپلود عکس", null=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار آگهی")
    publish = models.DateTimeField(default=timezone.now, verbose_name="تاریخ")
    update = models.DateTimeField(auto_now=timezone.now, verbose_name="بروزرسانی پست")
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='p', verbose_name="وضعیت")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(Advertise, self).save()

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

