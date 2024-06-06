from django.contrib import admin
from .models import UserProfile, Tweet, Hashtag

admin.site.register(UserProfile)
admin.site.register(Tweet)
admin.site.register(Hashtag)
