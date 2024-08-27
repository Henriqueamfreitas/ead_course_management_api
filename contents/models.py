from django.db import models


class Content(models.Model):
    name = models.CharField(max_length=150, null=False)
    content = models.CharField(null=False)
    video_url = models.CharField(max_length=200)
    course = models.ForeignKey(
        "contents.Content", on_delete=models.CASCADE, related_name="contents"
    )
