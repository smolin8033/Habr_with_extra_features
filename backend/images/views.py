from rest_framework.generics import ListCreateAPIView

from images.models import Image
from images.serializers import ImageSerializer


class ImageListCreateAPIView(ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
