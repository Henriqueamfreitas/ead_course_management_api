from django.db import models


class StudentCourseStatus(models.TextChoices):
    pending = "pending"
    accepted = "accepted"


class StudentCourse(models.Model):
    status = models.CharField(
        null=False,
        choices=StudentCourseStatus.choices,
        default=StudentCourseStatus.pending,
    )
    student = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        #
        related_name="students_courses",
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        #
        related_name="students_courses",
    )
