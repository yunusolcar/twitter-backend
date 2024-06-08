from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from .models import UserProfile, Tweet, Hashtag
from .serializers import UserProfileSerializer, TweetSerializer, HashtagSerializer


class UserProfileModelViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


class HashtagViewSet(ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer


class TweetModelViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        hashtag_name = self.request.query_params.get('hashtags')
        if hashtag_name:
            queryset = queryset.filter(hashtags__name=hashtag_name)
        return queryset
