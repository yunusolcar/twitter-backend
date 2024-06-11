from django.urls import path

from .views import UserProfileViewSet, UserDetailView

urlpatterns = [
    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
