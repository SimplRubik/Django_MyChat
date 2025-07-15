from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Room, Message



def room_list(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }

    return render(request, 'chat/room_list.html', context=context)

@login_required
def room_detail(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    messages = Message.objects.filter(room=room)
    context = {
        'room': room,
        'messages': messages,
    }
    
    return render(request, 'chat/room_detail.html', context=context)


