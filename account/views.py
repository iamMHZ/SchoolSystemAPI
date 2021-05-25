from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser

from account.serializers import StudentSerializer


class UserCreateView(CreateAPIView):
    """Create a new user base on the requested user"""

    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return self.serializer_class

        return StudentSerializer


class UserListView(ListAPIView):
    """List all the users in the database"""
    permission_classes = [IsAdminUser]

    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class CreateStudentView(CreateAPIView):
    """View for creating a new student"""
    # TODO auto fill is_student
    # TODO add the permission that a teacher can add a student
    # permission_classes =

    serializer_class = StudentSerializer


class ListStudentView(ListAPIView):
    """List the registered students for authenticated user"""

    # TODO add the permissions
    # permission_classes =

    serializer_class = StudentSerializer

    def get_queryset(self):
        return self.request.user.students.all()
