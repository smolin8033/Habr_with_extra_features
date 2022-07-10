from rest_framework.serializers import ModelSerializer

from images.serializers import ImageSerializer
from .models import Post


class PostReadSerializer(ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'body',
            'created_at',
            'images',
        )


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'body',
            'images',
        )
