from rest_framework import serializers
from .models import CustomUser, Post

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'body']
