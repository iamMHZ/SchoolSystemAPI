from rest_framework import serializers

from school import models


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ('teacher', 'title', 'body',)
