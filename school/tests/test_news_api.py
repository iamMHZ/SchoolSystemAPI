from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from school.models import News
from school.serializers import NewsSerializer

NEWS_URL = reverse('school:news-list')


class PublicNewsApiTest(APITestCase):
    """Test for the news api that does not demad authentication"""

    def setUp(self):
        self.client = APIClient()

    def test_news_needs_authentication(self):
        """Test that news api needs authentication"""

        response = self.client.get(NEWS_URL)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PrivateNewsApiTests(APITestCase):
    """Test for the new api that does not demand authentication"""

    def setUp(self):
        self.client = APIClient()
        self.teacher = get_user_model().objects.create_teacher(
            username='testTeacher',
            password='testpassword'
        )

        self.client.force_login(self.teacher)

    def test_retrieve_news(self):
        """Test that retrieving news is successful"""

        News.objects.create(teacher=self.teacher,
                            title='test title 1',
                            body='test body 1 ')

        News.objects.create(teacher=self.teacher,
                            title='test title 2 ',
                            body='test body 2 ')

        response = self.client.get(NEWS_URL)

        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_news_success(self):
        data = {
            'teacher': self.teacher.id,
            'title': 'test title',
            'body': 'teat body'
        }

        response = self.client.post(NEWS_URL, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        exits = News.objects.filter(**data).exists()
        self.assertTrue(exits)

    def test_create_news_with_invalid_data(self):
        """"Test creating a news with invalid data"""

        data = {'title': 'wrong payload should fail'}

        response = self.client.post(NEWS_URL, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
