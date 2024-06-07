# Generated by Django 5.0.6 on 2024-06-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtag',
            name='tweets',
        ),
        migrations.AddField(
            model_name='tweet',
            name='hashtag',
            field=models.ManyToManyField(blank=True, related_name='hashtag', to='tweets.hashtag'),
        ),
    ]
