from rest_framework import viewsets

from school import models
from school import serializers


class NewsViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
