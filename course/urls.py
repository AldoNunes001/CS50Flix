# 1. url / 2. view / 3. template

from django.contrib import admin
from django.urls import path, include
from .views import homepage

urlpatterns = [
    path('', homepage),
]