from rest_framework import serializers

from account.serializers import TeacherDetailSerializer
from school import models


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ('teacher', 'title', 'body',)


class NewsDetailedSerializer(NewsSerializer):
    teacher = TeacherDetailSerializer()
