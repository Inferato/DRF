from rest_framework import serializers
from .models import BlogPost, BlogComment
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = BlogComment
        fields = ['id', 'author', 'text']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post_comments = CommentSerializer(many=True, allow_null=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'created', 'author', 'text', 'post_comments']


class UserSerializer(serializers.ModelSerializer):

    post = PostSerializer(required=False, many=True, allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'post']


