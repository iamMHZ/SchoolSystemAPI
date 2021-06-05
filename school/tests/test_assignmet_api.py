from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

ASSIGNMENT_VIEWSET_URL = reverse('school:assignment-list')


class PublicAssignmentApiTest(APITestCase):
    """Tests for the assignments api that do not need authentication"""

    def setUp(self) -> None:
        self.client = APIClient()

    def test_assignment_api_needs_authentication(self):
        """Test that assignments api needs authentication"""

        response = self.client.get(ASSIGNMENT_VIEWSET_URL)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateAssignmentApiTest(APITestCase):
    """Tests for the assignmets api that need authentication"""
    # TODO add tests for listing creating and retrieving

    pass
