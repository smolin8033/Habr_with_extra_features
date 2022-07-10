from django.urls import path

from .views import PostListAPIView, PostCreateAPIView

urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/create/', PostCreateAPIView.as_view()),
]
