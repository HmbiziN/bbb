from actu.serializers import ActuSerializer, AlbumSerializer, PhotoSerializer
from actu.models import Actu, Album, Photo
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ActuViewSet(ModelViewSet):
    queryset = Actu.objects.all()
    serializer_class = ActuSerializer

    def get_queryset(self):
        return self.queryset[:10]


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
