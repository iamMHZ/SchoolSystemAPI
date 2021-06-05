from django.urls import include, path
from rest_framework.routers import DefaultRouter

from school.views import NewsViewSet, ListNewsView, AssignmentsViewSet

app_name = 'school'

router = DefaultRouter()
router.register('news', NewsViewSet)
router.register('assignments', AssignmentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list-my-news', ListNewsView.as_view(), name='list-my-news')
]
