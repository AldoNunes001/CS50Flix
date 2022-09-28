from django.contrib import admin
from .models import Course, Lecture, User
from django.contrib.auth.admin import UserAdmin

# To appear in the admin the field "open_courses"
fields = list(UserAdmin.fieldsets)
fields.append(
                ("History", {"fields": ("open_courses",)})
            )
UserAdmin.fieldsets = tuple(fields)

# [("Section Name", {"fields": ("first_field", "second_field")})]


# Register your models here.
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(User, UserAdmin)
