from django.shortcuts import render, redirect, reverse, get_object_or_404

from account.models import User
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse


def chats(request):
    return render(request, 'chat/chats.html')


def room_view(request, user1_id, user2_id):
    user = request.user
    if user.id == user1_id or user.id == user2_id:
        if user.is_authenticated:
            room_details = Room.objects.get(user_1_id=user1_id, user_2_id=user2_id)
            messages = room_details.room_messages.all()
            if request.method == 'POST':
                message = request.POST.get('message')
                user_id = request.POST.get('user_id')

                new_message = Message.objects.create(value=message, user_id=user_id, room_id=room_details.id)
                new_message.save()
            return render(request, 'chat/room.html', context={
                'user': user,
                'room_details': room_details,
                'messages': messages
            })
        else:
            return redirect('home:home')
    else:
        return redirect('home:home')


def check_view(request, user1_id, user2_id):
    if request.user.is_authenticated:
        if request.user.id == user1_id:
            if Room.objects.filter(user_1_id=user1_id, user_2_id=user2_id).exists():
                return redirect(reverse('chat:room', kwargs={'user1_id': user1_id, 'user2_id': user2_id}))
        if request.user.id == user2_id:
            if Room.objects.filter(user_1_id=user2_id, user_2_id=user1_id).exists():
                return redirect(reverse('chat:room', kwargs={'user1_id': user2_id, 'user2_id': user1_id}))
        else:
            Room.objects.create(user_1_id=user1_id, user_2_id=user2_id)
            return redirect(reverse('chat:room', kwargs={'user1_id': user1_id, 'user2_id': user2_id}))


