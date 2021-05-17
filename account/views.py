from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, CreateAPIView

from account.serializers import UserSerializer, SimpleUserSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return self.serializer_class

        return SimpleUserSerializer


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
