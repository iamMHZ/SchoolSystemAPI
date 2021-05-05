from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, password, **kwargs):
        pass

    def create_teacher(self, username, password, school_name, **kwargs):
        pass

    def create_student(self):
        pass

    def create_superuser(self, username, password, **kwargs):
        pass


class User(AbstractUser):
    # TODO add the national id field instead of username
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
