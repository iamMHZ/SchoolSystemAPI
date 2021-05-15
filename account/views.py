from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, CreateAPIView

from .serializers import UserSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
