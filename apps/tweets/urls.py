from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TweetViewSet, HashtagViewSet

router = DefaultRouter()
router.register(r'tweets', TweetViewSet)
router.register(r'hashtags', HashtagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
