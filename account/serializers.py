from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


# TODO  DRY

class UserSerializer(ModelSerializer):
    """Serializer with full access for all parameters of the custom model"""

    class Meta:
        model = get_user_model()
        fields = '__all__'


class SimpleUserSerializer(ModelSerializer):
    """serializer with for creating a simple user only (just active no permissions) """

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'password',)


class TeacherDetailSerializer(ModelSerializer):
    """detailed teacher serializer"""

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'school_name')
