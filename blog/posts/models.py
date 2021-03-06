from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', related_name='post', on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=500)

    class Meta:
        ordering = ['created']


class BlogComment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', related_name='comments', on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=250)
    post = models.ForeignKey('BlogPost', related_name='post_comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']



