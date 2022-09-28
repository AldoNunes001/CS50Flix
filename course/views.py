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

    def get(self, request, *args, **kwargs):
        course = self.get_object()
        course.views += 1
        course.save()

        return super().get(request, *args, **kwargs)  # Redirect user to url


    def get_context_data(self, **kwargs):
        context = super(Detailscourse, self).get_context_data(**kwargs)

        related_courses = self.model.objects.filter(category=self.get_object().category)[0:10]
        context['related_courses'] = related_courses

        return context


class Searchcourse(ListView):
    template_name = "searchcourse.html"
    model = Course

    def get_queryset(self):
        search_term = self.request.GET.get('query')

        if search_term:
            object_list = self.model.objects.filter(title__icontains=search_term)

            return object_list
