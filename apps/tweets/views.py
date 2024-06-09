from rest_framework import filters, status
from rest_framework.response import Response
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
        return queryset.filter(is_deleted=False)

    """
    when the tweet is deleted, the is_deleted field becomes True and does not appear on the screen
    """

    def soft_delete(self, request, *args, **kwargs):
        instance = self.get_object()
        delete_tweet = request.data.get('delete_tweet')
        if delete_tweet:
            instance.is_deleted = True
            instance.delete_tweet = delete_tweet
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
