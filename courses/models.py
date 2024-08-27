from django.db import models


class CourseStatus(models.TextChoices):
    not_started = ("not started",)
    in_progress = ("in progress",)
    finished = ("finished",)


class Course(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    status = models.CharField(
        null=False,
        choices=CourseStatus.choices,
        default=CourseStatus.not_started,
    )
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    instructor = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="courses"
    )
