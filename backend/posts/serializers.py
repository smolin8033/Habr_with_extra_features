from rest_framework.serializers import ModelSerializer

from .models import PostImage, Post


class PostImageSerializer(ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('post', 'image')


class PostSerializer(ModelSerializer):
    post_images = PostImageSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'body',
            'created_at',
            'post_images',
        )
