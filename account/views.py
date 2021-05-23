from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser

from account.serializers import UserSerializer, SimpleUserSerializer


class UserCreateView(CreateAPIView):
    """Create a new user base on the requested user"""

    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return self.serializer_class

        return SimpleUserSerializer


class UserListView(ListAPIView):
    """List all the users in the database"""
    permission_classes = [IsAdminUser]

    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class CreateStudentView(CreateAPIView):
    """View for creating a new student"""

    # TODO add the permission that a teacher can add a student
    # permission_classes =

    serializer_class = SimpleUserSerializer

    def perform_create(self, serializer):
        # if self.request.user.is_teacher:

        self.request.user.students.create(**serializer.data)


