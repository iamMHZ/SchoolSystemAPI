from django.urls import path

from .views import UserCreateView, UserListView, CreateStudentView, ListStudentView, AddStudentView

app_name = 'account'

urlpatterns = [

    # TODO two scope of django says: url "names" have underline instead of dashes
    path('create-account', UserCreateView.as_view(), name='create-account'),
    path('list-account', UserListView.as_view(), name='list-accounts'),

    path('create-student', CreateStudentView.as_view(), name='create-student'),
    path('add-student', AddStudentView.as_view(), name='add-student'),
    path('list-my-student', ListStudentView.as_view(), name='list-my-student'),

]
