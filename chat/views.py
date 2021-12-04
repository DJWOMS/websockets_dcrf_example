from asgiref.sync import sync_to_async
from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import User, Room, Message


def index(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        if name:
            room = Room.objects.create(name=name, host=request.user)
            print(room.pk)
            return HttpResponseRedirect(reverse("room", kwargs={"pk": room.pk}))
    return render(request, 'chat/index.html')


def room(request, pk):
    room: Room = get_object_or_404(Room, pk=pk)
    return render(request, 'chat/room.html', {
        "room": room,
    })


def test(request):
    return render(request, 'chat/test.html')
