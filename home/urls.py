from django.urls import path, re_path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>/<slug:slug>', views.detail, name='ad_detail'),
]
