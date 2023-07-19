from django.urls import path
from .views import UserDetailView,UserListView


urlpatterns = [
    path('userdetails/<int:pk>/', UserDetailView.as_view(), name='userdetails'),
    path('userlist/', UserListView.as_view(), name='userlist'),
]