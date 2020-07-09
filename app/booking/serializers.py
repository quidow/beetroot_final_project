from rest_framework import serializers

from .models import Amenity, Service, Hotel, HotelPhoto, Room, RoomPhoto, RoomPrice


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


class RoomPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPrice
        fields = ['id', 'date', 'price', ]


class RoomPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = ['id', 'photo', ]


class RoomReadSerializer(serializers.HyperlinkedModelSerializer):
    amenities = AmenitySerializer(many=True, read_only=True)
    prices = RoomPriceSerializer(many=True, read_only=True)
    photos = ImageUrlField(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'hotel', 'name', 'amenities', 'persons', 'prices', 'photos']


class RoomWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ['name', 'amenities', 'persons', ]


class HotelPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = ['id', 'photo', ]


class HotelReadSerializer(serializers.HyperlinkedModelSerializer):
    # photos = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='photo'
    # )
    services = ServiceSerializer(many=True, read_only=True)
    photos = ImageUrlField(many=True, read_only=True)
    rooms = RoomReadSerializer(many=True, read_only=True)

    # rooms = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='room-detail')
    # photos = HotelPhotoSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'services', 'rooms', 'photos']


class HotelWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'services', ]
