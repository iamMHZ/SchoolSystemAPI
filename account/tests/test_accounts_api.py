from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

CREATE_ACCOUNT_URL = reverse('account:create-account')
LIST_ACCOUNTS_URL = reverse('account:list-accounts')


class PublicAccountApiTests(APITestCase):
    """Test for account endpoints that do not need permissions or authentications """

    def setUp(self):
        self.client = APIClient()

    def test_create_superuser_needs_authentication(self):
        """Test that creating superuser needs authentication"""

        data = {
            'username': 'superuser',
            'password': 'passwordsuper',
            'is_superuser': True
        }

        response = self.client.post(CREATE_ACCOUNT_URL, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_users_needs_authentication(self):
        """Test that listing users needs authentication"""

        response = self.client.get(LIST_ACCOUNTS_URL)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateAccountApiTests(APITestCase):
    """Tests that need authentications for accessing accounts endpoints"""

    def setUp(self):
        # create a superuser
        self.user = get_user_model().objects.create_superuser(username='test',
                                                              password='password')
        self.client = APIClient()
        self.client.force_login(self.user)

    def test_create_superusers(self):
        """Test that creating a superuser with an unauthenticated user"""

        data = {
            'username': 'superuser',
            'password': 'passwordsuper',
            'is_superuser': True
        }

        response = self.client.post(CREATE_ACCOUNT_URL, data)

        superuser = get_user_model().objects.get(username=data['username'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(superuser.is_superuser)

    def test_listing_users_success(self):
        """Test listing users as an logedin superuser is successful"""

        response = self.client.get(LIST_ACCOUNTS_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_creating_students_success(self):
        """Test creating students is successful"""

        data = {
            'first_name': 'test first',
            'last_name': 'test last',
            'username': 'test_student',
            'password': 'test passs',
            'is_student': True
        }

        url = reverse('account:create-student')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        exists = get_user_model().objects.filter(username=data['username']).exists()

        self.assertTrue(exists)

    def test_listing_students_success(self):
        """Test listing students is successful"""

        data = {
            'first_name': 'test first',
            'last_name': 'test last',
            'username': 'test_student',
            'password': 'test passs',
            'is_student': True
        }

        url = reverse('account:create-student')
        self.client.post(url, data)

        url = reverse('account:list-my-student')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
