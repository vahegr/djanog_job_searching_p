from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chats, name='chats'),
    path('room/<int:user1_id>/<int:user2_id>/', views.room_view, name='room'),
    path('checkview/<int:user1_id>/<int:user2_id>/', views.check_view, name='check_view'),
]
