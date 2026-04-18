from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from .models import Room, Message
from .forms import RoomForm

@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'chat/room_list.html', {'rooms': rooms})

@login_required
def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    chat_messages = Message.objects.filter(room=room).order_by('timestamp')[:50]
    return render(request, 'chat/room_detail.html', {
        'room': room,
        'chat_messages': chat_messages,
    })

@login_required
def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            django_messages.success(request, 'Room created!')
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'chat/room_form.html', {'form': form})
# Create your views here.
