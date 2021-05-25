from rest_framework import serializers

from account.serializers import TeacherDetailSerializer
from school import models


class NewsSerializer(serializers.ModelSerializer):
    """Serializer for the news"""

    class Meta:
        model = models.News
        fields = ('teacher', 'title', 'body',)


class NewsDetailedSerializer(NewsSerializer):
    """Serializer for the news with detailed teacher data"""
    teacher = TeacherDetailSerializer()
