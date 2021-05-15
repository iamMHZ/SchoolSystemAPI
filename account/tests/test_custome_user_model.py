from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user_success(self):
        """Test creating a simple active user is successful"""

        username = 'test'
        password = '12345'

        user = get_user_model().objects.create_user(
            username=username,
            password=password,

        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_teacher)
        self.assertFalse(user.is_student)

    def test_create_superuser_success(self):
        """Test that creating a superuser is successful"""

        superuser = get_user_model().objects.create_superuser(
            username='test',
            password='12345'
        )

        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
