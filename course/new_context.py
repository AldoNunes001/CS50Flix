import random
from .models import Course


def recent_courses(request):
    lst_recent_courses = Course.objects.all().order_by('-creation_date')[0:8]

    return {"recent_courses": lst_recent_courses}


def popular_courses(request):
    lst_popular_courses = Course.objects.all().order_by('-views')[0:8]

    return {"popular_courses": lst_popular_courses}


def featured_course(request):
    courses = Course.objects.all()
    course = random.choice(courses)

    return {"featured_course": course}
