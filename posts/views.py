from rest_framework.generics import ListAPIView, CreateAPIView

from posts.models import Post
from posts.serializers import PostReadSerializer, PostSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostReadSerializer


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
