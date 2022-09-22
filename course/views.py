from django.shortcuts import render
from .models import Course
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.
class Homepage(TemplateView):
    template_name = "homepage.html"

# def homepage(request):
#     return render(request, "homepage.html")


class Homecourses(ListView):
    template_name = "homecourses.html"
    model = Course  # object_list -> model item list

# def homecourses(request):
#     context = {}
#     course_list = Course.objects.all()
#     context['course_list'] = course_list
#     return render(request, "homecourses.html", context)


class Detailscourse(DetailView):
    template_name = "detailscourse.html"
    model = Course  # object -> 1 item of model
