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
