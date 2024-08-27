from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    username = models.CharField(max_length=150, null=False, unique=True)
    password = models.CharField(max_length=128, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    is_superuser = models.BooleanField(default=False)
    my_courses = models.ManyToManyField(
        "courses.Course",
        through="students_courses.StudentCourse",
        related_name="students",
    )
