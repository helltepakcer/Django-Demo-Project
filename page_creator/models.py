from django.db import models
from django.utils import timezone


class PageCreator(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
