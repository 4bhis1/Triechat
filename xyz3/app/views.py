from django.shortcuts import redirect, render, HttpResponse
from app.models import Room, Message
from encrypt_code import encryption as ec
from encrypt_code import random_name as rn
from datetime import date
from datetime import datetime


def home(request):
    return render(request, 'home.html')


def create_private_room(request):
    return render(request, 'create_private_room.html')


def join_private_room(request):
    return render(request, 'join_private_room.html')


def public_chat(request):
    return render(request, 'public_chat.html')


def check_create_room(request):
    username = request.POST.get('Username')
    room = request.POST.get('room_name')
    password = request.POST.get('password')

    if Room.objects.filter(name=room).exists():
        return HttpResponse("From this name Room Already Exist")
    else:
        new_room = Room.objects.create(
            name=room, password=password)
        new_room.save()
        return redirect('/' + room + '/' + username)


def check_join_room(request):
    username = request.POST.get('Username')
    room = request.POST.get('room_name')
    password = request.POST.get('password')

    if Room.objects.filter(name=room).exists():
        if Room.objects.filter(name=room, password=password):
            return redirect('/' + room + '/' + username)
        else:
            return HttpResponse('Wrong Password')
    else:
        return HttpResponse('Room Does Not Exist')


def check_public_chat(request):
    if request.method == 'POST':
        room = 'common'
        username = request.POST.get('Username')
        if Room.objects.filter(name=room).exists():
            print(room)
            print(username)
            return redirect('/' + room + '/' + username)
        else:
            new_room = Room.objects.create(
                name=room, password=1234)
            new_room.save()
            return redirect('/' + room + '/' + username)
    return render(request, 'public_chat.html')


def room(request, room, username):
    messagelist = Message.objects.filter(room=room).values()
    room_details = Room.objects.get(name=room)
    roomlist = Room.objects.all()
    if request.method == 'POST':

        if request.POST.get('Username'):
            username = request.POST.get('Username')
            room = request.POST.get('room_name')
            password = request.POST.get('password')

            if Room.objects.filter(name=room).exists():
                if Room.objects.filter(name=room, password=password):
                    return redirect('/' + room + '/' + username)
                else:
                    return HttpResponse('Wrong Password')
            else:
                return HttpResponse('Room Does Not Exist')

        else:
            msg = request.POST['message']
            try:
                file = request.FILES["file"]
            except:
                file = ''

            if msg != '' or file != '':
                today = date.today().strftime("%Y-%m-%d")
                time = datetime.now().strftime('%H:%M:%S')

                message = Message(room=room, user=username, msg=msg,
                                  file=file, time=time, date=today)
                message.save()

        return render(request, 'room.html', {
            'roomlist': roomlist,
            'message': messagelist,
            'username': username,
            'room': room,
            'room_details': room_details
        })

    return render(request, 'room.html', {
        'roomlist': roomlist,
        'message': messagelist,
        'username': username,
        'room': room,
        'room_details': room_details
    })
