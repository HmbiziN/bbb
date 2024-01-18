from actu.models import Actu, Album, Photo
from rest_framework import serializers


class ActuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actu
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    total_photos = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = "__all__"

    def get_photos(self, instance):
        try:
            photos = Photo.objects.filter(album=instance)
            serializer = PhotoSerializer(photos, many=True)
            return serializer.data
        except:
            pass

    def get_total_photos(self, instance):
        try:
            len_photos = Photo.objects.filter(album=instance).count()
            return len_photos
        except:
            pass


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"
