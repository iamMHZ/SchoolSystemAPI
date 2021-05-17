from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """Serializer with full access for all parameters of the custom model"""

    class Meta:
        model = get_user_model()
        fields = '__all__'


class SimpleUserSerializer(ModelSerializer):
    """A serializer with for creating a simple user only """

    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)
