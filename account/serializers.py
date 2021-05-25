from django.contrib.auth import get_user_model
from rest_framework import serializers


# TODO  DRY

class UserSerializer(serializers.ModelSerializer):
    """Serializer with full access for all parameters of the custom model"""

    class Meta:
        model = get_user_model()
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
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
        # TODO add an endpoint for creating students without needs of a teacher being logged in
        return student


class TeacherDetailSerializer(serializers.ModelSerializer):
    """detailed teacher serializer"""

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'school_name')


# TODO BUG  'str' object has no attribute 'username'
class AddStudentSerializer(serializers.Serializer):
    """Serializer that enabels the curent user 'add' a student to its students  """

    username = serializers.CharField(max_length=150)

    def create(self, validated_data):
        # lock up the user and determine that it actually exits
        student = get_user_model().objects.get(username=validated_data.get('username'))

        if student:
            # TODO what to do with the already added students
            self.context['request'].user.students.add(student)
            return validated_data.get('username')

        else:
            return 'student has not registered yet '
