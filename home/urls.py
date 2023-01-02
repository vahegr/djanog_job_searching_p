from django.urls import path, re_path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/', views.detail, name='ad_detail'),
    path("search_result/", views.search_result, name='search result'),
    path("my_advertises/", views.my_advertises, name='my advertises'),
    path("add_advertise/", views.add_advertise, name='add advertise'),
    path("edit_resume/<str:username>", views.edit_resume, name='edit resume'),
    path("resume_detail/<int:user_id>", views.resume_detail, name='resume detail'),
]
