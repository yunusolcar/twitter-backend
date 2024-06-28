from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegisterView, LoginView, ProfileView, UserProfileViewSet, UserDetailView

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/profile/', ProfileView.as_view(), name='profile'),
    path('auth/user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('', include(router.urls)),
]
