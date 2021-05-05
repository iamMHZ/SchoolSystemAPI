from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_teacher(self):
        pass

    def create_student(self):
        pass

    def create_superuser(self):
        pass


class User(AbstractUser):
    school_name = models.CharField(max_length=255, null=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    is_active = False
    is_staff = False
    is_superuser = False

    # USERNAME_FIELD = 'national id'
    # REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username
