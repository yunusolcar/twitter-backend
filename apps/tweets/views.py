from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Tweet, Hashtag
from .serializers import TweetSerializer, HashtagSerializer


class TweetModelViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']
    permission_classes = [IsAuthenticated]


class HashtagViewSet(ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
    permission_classes = [IsAuthenticated]
