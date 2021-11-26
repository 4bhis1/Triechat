from django.db import models


class User(models.Model):
    user_name=models.CharField(max_length=100,unique=True,blank=False)
    profile_photo=models.ImageField(upload_to='media/dp',max_length=100,blank=True)
    
class Room(models.Model):
    name=models.CharField(max_length=100,unique=True,blank=False)
    password=models.CharField(max_length=100,blank=False)
    profile_photo=models.ImageField(upload_to='media/file',max_length=100,blank=True)
    admin=models.CharField(max_length=100,blank=False)
    
class Message(models.Model):
    room=models.CharField(max_length=100,blank=False)
    user=models.CharField(max_length=100,blank=False)
    msg=models.CharField(max_length=100000,blank=True)
    file=models.FileField(upload_to='media/file',max_length=1000,blank=True)
    time=models.TimeField(blank=False)
    date=models.DateField(blank=False)
    
    
# username = absk
# password = 1234
# emailid = 4bhis1@gmail.com