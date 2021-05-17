from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from account.serializers import SimpleUserSerializer

CREATE_ACCOUNT_URL = reverse('create-account')
LIST_ACCOUNTS_URL = reverse('list-accounts')


class PublicAccountTest(APITestCase):
    """Test for account endpoints that do not need permissions or authentications """

    def setUp(self):
        self.client = APIClient()

    def test_create_simple_user_success(self):
        """Test that an unauthenticated user can only create a simple active use with no special privilege"""

        data = {
            'username': 'testuser',
            'password': 'testpass',
        }

        response = self.client.post(CREATE_ACCOUNT_URL, data)

        simple_user = get_user_model().objects.get(username=data['username'])
        serializer = SimpleUserSerializer(simple_user)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)

        self.assertTrue(simple_user.is_active)
        self.assertFalse(simple_user.is_superuser)
        self.assertFalse(simple_user.is_staff)
        self.assertFalse(simple_user.is_teacher)
        self.assertFalse(simple_user.is_student)

    def test_create_superusers(self):
        """Test that creating a superuser with an unauthenticated user"""

        data = {
            'username': 'superuser',
            'password': 'passwordsuper',
            'is_superuser': True
        }

        response = self.client.post(CREATE_ACCOUNT_URL, data)

        simple_user = get_user_model().objects.get(username=data['username'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(simple_user.is_superuser)

    def test_list_users_needs_authentication(self):
        """Test that listing users needs authentication"""

        response = self.client.get(LIST_ACCOUNTS_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
