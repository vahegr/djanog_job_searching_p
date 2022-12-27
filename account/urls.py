from django.urls import path, re_path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
]
