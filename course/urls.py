# 1. url / 2. view / 3. template

from django.contrib import admin
from django.urls import path, include, reverse_lazy
from .views import Homepage, Homecourses, Detailscourse, Searchcourse, Editprofile, Createaccount
from django.contrib.auth import views as auth_view

app_name = 'course'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('courses/', Homecourses.as_view(), name='homecourses'),
    path('courses/<int:pk>', Detailscourse.as_view(), name='detailscourse'),  # <int:pk>  <type:primary_key>
    path('searchcourse/', Searchcourse.as_view(), name='searchcourse'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editprofile/<int:pk>', Editprofile.as_view(), name='editprofile'),
    path('createaccount/', Createaccount.as_view(), name='createaccount'),
    path('changepassword/', auth_view.PasswordChangeView.as_view(template_name='editprofile.html', success_url=reverse_lazy('course:homecourses')), name='changepassword'),
]
