# 1. url / 2. view / 3. template

from django.contrib import admin
from django.urls import path, include
from .views import Homepage, Homecourses, Detailscourse

urlpatterns = [
    path('', Homepage.as_view()),
    path('courses', Homecourses.as_view()),
    path('courses/<int:pk>', Detailscourse.as_view())  # <int:pk>  <type:primary_key>
]
