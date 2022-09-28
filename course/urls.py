# 1. url / 2. view / 3. template

from django.contrib import admin
from django.urls import path, include
from .views import Homepage, Homecourses, Detailscourse, Searchcourse

app_name = 'course'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('courses/', Homecourses.as_view(), name='homecourses'),
    path('courses/<int:pk>', Detailscourse.as_view(), name='detailscourse'),  # <int:pk>  <type:primary_key>
    path('searchcourse/', Searchcourse.as_view(), name='searchcourse'),
]
