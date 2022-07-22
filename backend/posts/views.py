from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.models import Post, PostImage
from posts.serializers import PostSerializer
from users.models import User


@extend_schema(tags=['Posts'])
class PostViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        try:
            author_id = request.data.get('author', request.user.id)
            author = get_object_or_404(User, id=author_id)

            title = request.data['title']
            body = request.data['body']
            image_fields = request.data.getlist('image')

            post = Post(
                author=author,
                title=title,
                body=body
            )
            post.save()

            for image in image_fields:
                post_image = PostImage(
                    post=post,
                    image=image
                )
                post_image.save()

            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        # try:
        post = get_object_or_404(Post, pk=kwargs['pk'])
        post_images = post.post_images.all()
        images = request.data.getlist('image')
        print([i for i in post_images])
        print([i for i in images])

        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # except Exception:
            # return Response(status=status.HTTP_400_BAD_REQUEST)
