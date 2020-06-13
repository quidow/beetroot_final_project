from rest_framework import serializers
from .models import Amenity, Service, Hotel, Room


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ['pk', 'name', ]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['pk', 'name', ]


class HotelSerializer(serializers.ModelSerializer):
    # services = ServiceSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ['pk', 'name', 'services', ]


class RoomSerializer(serializers.ModelSerializer):
    # amenities = AmenitySerializer(many=True)

    class Meta:
        model = Room
        fields = ['pk', 'hotel', 'amenities', 'persons']
