from rest_framework import permissions
from rest_framework import viewsets

from school import models
from school import serializers


class NewsViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = permissions.IsAuthenticated

    def get_queryset(self):
        """limit the news to the authenticated user"""
        return self.queryset.filter(teacher=self.request.user)
