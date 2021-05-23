from django.urls import path

from .views import UserCreateView, UserListView, CreateStudentView, ListStudentView

app_name = 'account'

urlpatterns = [

    path('create-account', UserCreateView.as_view(), name='create-account'),
    path('list-account', UserListView.as_view(), name='list-accounts'),

    path('add-student', CreateStudentView.as_view(), name='add-student'),
    path('list-my-student', ListStudentView.as_view(), name='list-my-student'),

]
