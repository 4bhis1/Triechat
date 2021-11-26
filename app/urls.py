from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.home),
    path('<str:room>/<str:user>',views.common),
    path('r/<str:room>/<str:user>',views.room),
    path('c/<str:room>/<str:password>',views.check)
]
