from rest_framework import serializers
from posts.models import Post
from user.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['id','title', 'content', 'slug', 'miniature', 'created', 'published', 'user', 'category']