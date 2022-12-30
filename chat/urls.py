from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chats, name='chats'),
    path('<str:room>/<str:user1_username>/<str:user2_username>/', views.room_view, name='room'),
    path('checkview/<str:user1_username>/<str:user2_username>/', views.check_view, name='check_view'),
    path('send', views.send, name='send'),
    path('get_messages/<str:room>/', views.get_messages, name='get_messages'),
]
