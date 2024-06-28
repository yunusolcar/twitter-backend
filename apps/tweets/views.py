from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthorOrReadOnly

from .models import Tweet, Hashtag
from .serializers import TweetSerializer, HashtagSerializer


class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        hashtag_name = self.request.query_params.get('hashtag')
        if hashtag_name:
            queryset = queryset.filter(hashtags__name=hashtag_name)
        return queryset


class HashtagViewSet(ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    permission_classes = [IsAuthenticated]
