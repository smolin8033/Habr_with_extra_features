from rest_framework.fields import ImageField
from rest_framework.serializers import ModelSerializer

from .models import PostImage, Post


class PostImageSerializer(ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('image',)


class PostSerializer(ModelSerializer):
    images = PostImageSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'author',
            'title',
            'body',
            'created_at',
            'images'
        )


class PostCreateSerializer(ModelSerializer):
    image = ImageField()

    class Meta:
        model = Post
        fields = (
            'title',
            'body',
            'image'
        )
