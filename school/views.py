from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from school import models
from school import serializers


class NewsViewSet(viewsets.ModelViewSet):
    """ViewSet for the news that teachers can can list retrieve, create ... their news """

    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    # TODO add the teacher only permission
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """limit the news to the authenticated user"""
        return self.queryset.filter(teacher=self.request.user)

    def perform_create(self, serializer):
        """Save the news for the authenticated user"""
        serializer.save(teacher=self.request.user)

    def get_serializer_class(self):
        """Change the serializer based on the action"""
        if self.action == 'retrieve':
            return serializers.NewsDetailedSerializer

        return self.serializer_class


class ListNewsView(ListAPIView):
    """View for a student to retrieve their teachers news"""

    # TODO add permission

    serializer_class = serializers.NewsSerializer

    def get_queryset(self):
        """Get news only for the logged in student(user)"""
        student = self.request.user
        # Retrieve the news for the student
        teachers_of_student = get_user_model().objects.filter(students=student).all()
        news = models.News.objects.filter(teacher__id__in=teachers_of_student).all()

        return news


class AssignmentsViewSet(viewsets.ModelViewSet):
    """ViewSet for teacher that enables them to manipulate their assignments"""
    queryset = models.Assignment.objects.all()
    serializer_class = serializers.AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        """Only return the news for the current logged in user"""
        return models.Assignment.objects.filter(teacher=self.request.user)

    def perform_create(self, serializer):
        """Save the assignment only for the current loged in user"""
        serializer.save(teacher=self.request.user)
