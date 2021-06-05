from django.conf import settings
from django.db import models


class AbstractBaseTask(models.Model):
    """Abstract base task that has all the common fields of the new and assignment """

    teacher = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=600)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, )

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.title)


class News(AbstractBaseTask):
    """Model for the News"""
    pass


class Assignment(AbstractBaseTask):
    """Model for the Assignments"""
    pass
    # TODO add pdf file to assignment
    # TODO add answers to assignments
    # file =
