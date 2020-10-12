from rest_framework import serializers
from .models import BlogPost, BlogComment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = BlogComment
        fields = ['id', 'author', 'text', 'posts']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comment = CommentSerializer(required=False, many=True, allow_null=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'created', 'author', 'text', 'comment']
        depth = 3
