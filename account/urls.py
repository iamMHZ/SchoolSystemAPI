from django.urls import path

from .views import UserCreateView, UserListView

urlpatterns = [

    path('create-user', UserCreateView.as_view()),
    path('list-user', UserListView.as_view()),

]
