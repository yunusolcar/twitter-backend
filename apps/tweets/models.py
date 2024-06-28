from django.db import models

from apps.users.models import UserProfile

"""
Hashtag Model
"""


class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


"""
Tweet Model
"""


class Tweet(models.Model):
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, related_name='tweets', on_delete=models.CASCADE)
    hashtags = models.ManyToManyField(Hashtag, related_name='tweets', blank=True, )

    def __str__(self):
        return f"{self.author.username}"
