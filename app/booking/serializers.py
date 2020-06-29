from django.conf import settings
from rest_framework import serializers

from .models import Amenity, Service, Hotel, HotelPhoto, Room, RoomPhoto


class ImageUrlField(serializers.RelatedField):
    def to_representation(self, instance):
        url = instance.photo.url
        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(url)
        return url


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['id', 'name', 'description', 'icon', ]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'icon', ]


class HotelPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = ['id', 'photo', ]


class HotelSerializer(serializers.ModelSerializer):
    # photos = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='photo'
    # )
    photos = ImageUrlField(many=True, read_only=True)

    # photos = HotelPhotoSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'services', 'photos']


class RoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = ['id', 'photo', 'room', ]


class RoomSerializer(serializers.ModelSerializer):
    photos = ImageUrlField(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'hotel', 'amenities', 'persons', 'photos']
