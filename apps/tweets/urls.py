from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserProfileModelViewSet, TweetModelViewSet

router = DefaultRouter()
router.register(r'tweets', TweetModelViewSet)
router.register(r'users', UserProfileModelViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
