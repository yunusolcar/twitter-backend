from rest_framework import serializers

from .models import Tweet, Hashtag


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'content', 'created_at', 'author', 'hashtags']
        read_only_fields = ['author']


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['id', 'name']