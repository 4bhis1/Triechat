"""xyz3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),


    # home
    path('', views.home, name='home'),

    # creating private room
    path('create_private_room', views.create_private_room,
         name='create_private_room'),
    path('check_create_room', views.check_create_room,
         name='check_create_room'),

    # joining private room
    path('join_private_room', views.join_private_room, name='join_private_room'),
    path('check_join_room', views.check_join_room,
         name='check_join_room'),

    # public chat
    path('public_chat', views.public_chat, name='public_chat'),
    path('check_public_chat', views.check_public_chat, name='check_public_chat'),

    path('<str:room>/<str:username>', views.room),
]
