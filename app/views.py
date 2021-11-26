from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .python_code import random_name as rn
from .python_code import encryption as ec
from app.models import Room,User,Message

from datetime import date
from datetime import datetime


today=date.today().strftime('%d %b %y')
time=datetime.now().strftime('%H : %M:%S')

# Create your views here.

def home(request):
    k=str(rn.random_name())
    
    t=User(user_name=k)
    t.save()
    
    st=ec.encrypt(k)
    print(k)
    room=ec.encrypt('common')
    
    return redirect(room+'/'+st)


def common(request,room,user):
    
    room=ec.decrypt(room)
    user=ec.decrypt(user)
    
    roomlist=Room.objects.all()
    userlist=User.objects.all()
    messagelist=Message.objects.filter(room=room).values()
    
    if request.method=="POST":
        
        if request.POST.get('User_name'):
            
            k=request.POST['User_name']
            
            u=User.objects.get(user_name=user)
            u.user_name=k
            
            u.save()
            
            room=ec.encrypt('common')
            st=ec.encrypt(k)
    
            return render(request,"main.html",{'room':room,'user':user,'roomlist':roomlist,'userlist':userlist,'message':messagelist})
        
        elif request.POST.get('Room_name'):
            
            rname=request.POST['Room_name']
            passw=request.POST['Password']
            
            r=Room(name=rname,password=passw,admin=user)
            r.save()
            
        elif request.POST.get("user_password"):
            
            userPassword=request.POST["user_password"]
            userRoom=request.POST["room_name"]
            
            if Room.objects.filter(name=userRoom,password=userPassword):
                return redirect("/r/"+userRoom+"/"+user)

            else:
                return HttpResponse("<h1>Wrong password")
            
        else:
            try:
                file=request.FILES["media"]
            except:
                file=''
            msg=request.POST["msg"]
            
            today=date.today().strftime("%Y-%m-%d")
            time=datetime.now().strftime('%H:%M:%S')
            
            t=Message(room=room,user=user,msg=msg,file=file,time=time,date=today)
            t.save()
            
            return render(request,"main.html",{'room':room,'user':user,'roomlist':roomlist,'userlist':userlist,'message':messagelist})
    
    
    return render(request,"main.html",{'room':room,'user':user,'roomlist':roomlist,'userlist':userlist,'message':messagelist})   


def room(request,room,user):
      
    t=Room.objects.filter(name=room).values('password')
    # t=t['password']
    t="http://c/"+room+"/"+str(t)
    # print(t)
      
    
    if request.method=="POST":
        try:
            file=request.FILES["media"]
        except:
            file=''
        msg=request.POST["msg"]
        
        today=date.today().strftime("%Y-%m-%d")
        time=datetime.now().strftime('%H:%M:%S')
        
        t=Message(room=room,user=user,msg=msg,file=file,time=time,date=today)
        t.save()
        
    t=Room.objects.filter(name=room).values('password')
    # t=t['password']
    t="http://c/"+room+"/"+str(t)
    # print(t)
    
    messagelist=Message.objects.filter(room=room).values()
    
    return render(request,'room.html',{"room":room,"user":user,"URL":t,"message":messagelist})


def check(request,room,password):
    
    if Room.objects.filter(name=room,password=password):
        
        return redirect("/r/"+room+"/"+str(rn.random_name()))
    
    else:
        
        return HttpResponse("<h1> Wrong URL")