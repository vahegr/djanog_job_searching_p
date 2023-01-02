from django import forms
from .models import Advertise, Category
from account.models import User


class AddAdvertiseForm(forms.ModelForm):
    title = forms.CharField(max_length=150, label='موضوع')
    slug = forms.CharField(max_length=150, label='آدرس آگهی')
    name = forms.CharField(max_length=100, label='نام')
    phone = forms.CharField(max_length=11, label='شماره تماس')
    email = forms.EmailField(max_length=100, label='ایمیل')
    company = forms.CharField(max_length=100, label='شرکت')
    city = forms.CharField(max_length=100, label='شهر')
    description = forms.CharField(max_length=9000, label='متن آگهی')
    thumbnail = forms.ImageField(label='آپلود عکس')

    class Meta:
        model = Advertise
        fields = (
            'title', 'slug', 'name', 'phone', 'email',
            'company', 'city', 'description', 'thumbnail', 'category')


class EditResumeForm(forms.ModelForm):
    image = forms.ImageField(label='تصویر', required=False)

    class Meta:
        model = User
        fields = '__all__'
        exclude = ('type_of_user', 'password', 'last_login', 'is_active', 'is_admin')
