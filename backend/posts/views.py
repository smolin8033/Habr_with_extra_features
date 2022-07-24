from collections import OrderedDict

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.models import Post, PostImage
from posts.serializers import PostCreateSerializer, PostSerializer
from users.models import User


@extend_schema(tags=['Posts'])
class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def get_serializer_class(self):
        serializer_class = PostSerializer
        if self.action == 'create':
            serializer_class = PostCreateSerializer
        return serializer_class

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        print(serializer.initial_data)
        serializer.is_valid(raise_exception=True)

        print(serializer)
        print(serializer.data)
        data: OrderedDict = serializer.validated_data
        print(data)
        # image = data.pop('image')
        # post = self.post_create(**data)
        # self.image_create(post, image)
        #
        # return Response(data, status=status.HTTP_201_CREATED)

    def post_create(self, **data):
        post = Post.objects.create(**data, author=self.request.user)
        return post

    def image_create(self, post, image):
        image = PostImage.objects.create(post=post, image=image)
        return image

    def update(self, request, *args, **kwargs):
        # try:
        post = get_object_or_404(Post, pk=kwargs['pk'])
        post_images = post.post_images.all()
        images = request.data.getlist('image')
        print([i for i in post_images])
        print([i for i in images])

        # serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # except Exception:
            # return Response(status=status.HTTP_400_BAD_REQUEST)
