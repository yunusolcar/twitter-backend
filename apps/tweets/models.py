from django.db import models

"""
UserProfile Model
"""


class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


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
    hashtag = models.ManyToManyField(Hashtag, blank=True,)

    def __str__(self):
        return f"{self.author.username}"
