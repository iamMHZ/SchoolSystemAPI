from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Manger for creating user objects"""

    def create_user(self, username, password, **kwargs):
        """Creates a simple active user with no permissions"""
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_teacher(self, username, password, **kwargs):
        """Creates a teacher"""
        user = self.create_user(username, password, **kwargs)
        user.is_teacher = True
        user.save(using=self._db)

        return user

    def create_student(self, username, password, **kwargs):
        """Creates a student"""

        user = self.create_user(username, password, **kwargs)
        user.is_student = True
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **kwargs):
        """Creates a superuser """

        user = self.create_user(username, password, **kwargs)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractUser):
    """A user model that supports students and teacher flags and has the national id field"""

    # TODO add the national id field instead of username
    school_name = models.CharField(max_length=255, blank=True)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return self.username
