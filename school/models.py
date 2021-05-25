from django.conf import settings
from django.db import models


class News(models.Model):
    teacher = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=600)

    def __str__(self):
        return str(self.title)

# class Assignment(models.Model):
#     pass


# class Task(models.Model):
#     pass
