from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

# (DB, user)
CATEGORIES = (
    ("CS", "Computer Science"),
    ("PYTHON", "Python"),
    ("WEB", "Web"),
    ("JAVASCRIPT", "JavaScript"),
    ("AI", "Artificial Intelligence"),
    ("GD", "Game Development"),
    ("MAD", "Mobile App Development"),
)


# Create course
class Course(models.Model):
    title = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to="thumb_courses")
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=30, choices=CATEGORIES)
    views = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Create lecture
class Lecture(models.Model):
    # course = models.ManyToManyField()
    course = models.ForeignKey('Course', related_name='lectures', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.course.title + ' / ' + self.title


# Create user
class User(AbstractUser):
    open_courses = models.ManyToManyField("Course")
