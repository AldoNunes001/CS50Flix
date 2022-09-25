from .models import Course

def recent_courses(request):
    lst_recent_courses = Course.objects.all().order_by('-creation_date')[0:10]

    return {"recent_courses": lst_recent_courses}


def popular_courses(request):
    lst_popular_courses = Course.objects.all().order_by('-views')[0:10]

    return {"popular_courses": lst_popular_courses}
