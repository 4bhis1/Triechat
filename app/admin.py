from django.contrib import admin

from .models import Room,User,Message

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(User)