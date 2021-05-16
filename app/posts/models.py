import uuid

from django.db import models
from django.urls import reverse


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=200)
    description_long = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to="covers/", default="project.png")
    description_alt = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
