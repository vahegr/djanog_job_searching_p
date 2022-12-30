from django.shortcuts import render, redirect, reverse
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse


def chats(request):
    return render(request, 'chat/chats.html')


def room_view(request, room, user1_username, user2_username):
    user = request.user
    if user.username == user1_username:
        room_details = Room.objects.get(name=room, user_1__username=user1_username, user_2__username=user2_username)
        return render(request, 'chat/room.html', context={
            'user': user,
            'room': room,
            'room_details': room_details
        })
    else:
        return redirect('home:home')


def check_view(request, room, user1_username, user2_username):
    if Room.objects.filter(name=room, user_1__username=user1_username, user_2__username=user2_username).exists():
        return redirect(reverse('chat:room', kwargs={'room': room, 'user1_username': user1_username, 'user2_username': user2_username}))
    else:
        Room.objects.create(
            name=f"{user1_username}-{user2_username}",
            user_1__username=user1_username, user_2__username=user2_username)
        return redirect(reverse('chat:room', kwargs={'room': room, 'user1_username': user1_username, 'user2_username': user2_username}))


def send(request):
    message = request.POST['message']
    userid = request.POST['userid']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user_id=userid, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def get_messages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})
