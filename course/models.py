from django.db import models
from django.utils import timezone

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



# Create week/episode

# Create user
