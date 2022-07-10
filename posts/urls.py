from django.urls import path

from .views import (
    PostListAPIView,
    PostCreateAPIView,
    PostRetrieveAPIView,
    PostUpdateAPIView,
    PostDestroyAPIView,
)

urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>/', PostRetrieveAPIView.as_view()),
    path('posts/<int:pk>/update/', PostUpdateAPIView.as_view()),
    path('posts/<int:pk>/delete/', PostDestroyAPIView.as_view()),
    path('posts/create/', PostCreateAPIView.as_view()),
]
