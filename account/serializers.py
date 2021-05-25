from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


# TODO  DRY

class UserSerializer(ModelSerializer):
    """Serializer with full access for all parameters of the custom model"""

    class Meta:
        model = get_user_model()
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    """serializer with for creating a student """

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'password', 'is_student')
        # TODO if write only then the CreateStudentView doesnt get the password
        # TODO if not write only then the raw password can be seen
        # TODO to be or not to be
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create a student and then add the student to the current user"""
        student = get_user_model().objects.create_student(**validated_data)
        self.context['request'].user.students.add(student)

        return student


class TeacherDetailSerializer(ModelSerializer):
    """detailed teacher serializer"""

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'school_name')
