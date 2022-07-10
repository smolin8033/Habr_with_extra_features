from django.urls import path

from .views import ImageListCreateAPIView

urlpatterns = [
    path('images/', ImageListCreateAPIView.as_view()),
]
