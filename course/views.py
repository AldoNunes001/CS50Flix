from django.shortcuts import render
from .models import Course


# Create your views here.
def homepage(request):
    return render(request, "homepage.html")


def homecourses(request):
    context = {}
    course_list = Course.objects.all()
    context['course_list'] = course_list
    return render(request, "homecourses.html", context)
