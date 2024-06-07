from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from .serializers import UserProfileSerializer, TweetSerializer, HashtagSerializer
from .models import UserProfile, Tweet, Hashtag


class UserProfileModelViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


class TweetModelViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']


class HashtagViewSet(ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
