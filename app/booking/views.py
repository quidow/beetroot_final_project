from rest_framework import viewsets
from .models import Amenity, Service, Hotel, HotelPhoto, Room, RoomPhoto
from .serializers import AmenitySerializer, ServiceSerializer, HotelSerializer, HotelPhotoSerializer, RoomSerializer, \
    RoomPhotoSerializer


class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelPhotoViewSet(viewsets.ModelViewSet):
    queryset = HotelPhoto.objects.all()
    serializer_class = HotelPhotoSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomPhotoViewSet(viewsets.ModelViewSet):
    queryset = RoomPhoto.objects.all()
    serializer_class = RoomPhotoSerializer
