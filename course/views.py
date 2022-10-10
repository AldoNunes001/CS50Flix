from django.shortcuts import render, redirect, reverse
from .models import Course, User
from .forms import CreateAccountForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('course:homecourses')

        else:
            return super().get(request, *args, **kwargs)  # Redirect to homepage

    def get_success_url(self):
        email = self.request.POST.get('email')
        user = User.objects.filter(email=email)

        if user:
            return reverse('course:login')
        else:
            return reverse('course:createaccount')

# def homepage(request):
#     return render(request, "homepage.html")


class Homecourses(LoginRequiredMixin, ListView):
    template_name = "homecourses.html"
    model = Course  # object_list -> model item list

# def homecourses(request):
#     context = {}
#     course_list = Course.objects.all()
#     context['course_list'] = course_list
#     return render(request, "homecourses.html", context)


class Detailscourse(LoginRequiredMixin, DetailView):
    template_name = "detailscourse.html"
    model = Course  # object -> 1 item of model

    def get(self, request, *args, **kwargs):
        course = self.get_object()
        course.views += 1
        course.save()

        user = request.user
        user.viewed_courses.add(course)

        return super().get(request, *args, **kwargs)  # Redirect user to url


    def get_context_data(self, **kwargs):
        context = super(Detailscourse, self).get_context_data(**kwargs)

        related_courses = self.model.objects.filter(category=self.get_object().category)[0:10]
        context['related_courses'] = related_courses

        return context


class Searchcourse(LoginRequiredMixin, ListView):
    template_name = "searchcourse.html"
    model = Course

    def get_queryset(self):
        search_term = self.request.GET.get('query')

        if search_term:
            object_list = self.model.objects.filter(title__icontains=search_term)

            return object_list


class Editprofile(LoginRequiredMixin, UpdateView):
    template_name = 'editprofile.html'
    model = User
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('course:homecourses')


class Createaccount(FormView):
    template_name = 'createaccount.html'
    form_class = CreateAccountForm

    def form_valid(self, form):
        form.save()

        messages.success(self.request, f'Your account was created!')

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('course:homecourses')

