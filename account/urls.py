from django.urls import path

from .views import UserCreateView, UserListView

urlpatterns = [

    path('create-account', UserCreateView.as_view()),
    path('list-account', UserListView.as_view()),

]
