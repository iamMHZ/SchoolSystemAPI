from django.urls import include, path
from rest_framework.routers import DefaultRouter

from school.views import NewsViewSet, ListNewsView

app_name = 'school'

router = DefaultRouter()
router.register('news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list-my-news', ListNewsView.as_view(), name='list-my-news')
]
