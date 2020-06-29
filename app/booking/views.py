from rest_framework import permissions
from rest_framework import viewsets

from .models import Amenity, Service, Hotel, HotelPhoto, Room, RoomPhoto
from .permissions import IsOwnerOrReadOnly, IsSuperUserOrReadOnly, IsOwnerOrReadOnlyHotelRel, \
    IsOwnerOrReadOnlyHotelRoomRel
from .serializers import AmenitySerializer, ServiceSerializer, HotelSerializer, HotelPhotoSerializer, RoomSerializer, \
    RoomPhotoSerializer


class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [IsSuperUserOrReadOnly]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsSuperUserOrReadOnly]


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owners=[self.request.user])


class HotelPhotoViewSet(viewsets.ModelViewSet):
    queryset = HotelPhoto.objects.all()
    serializer_class = HotelPhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyHotelRel]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyHotelRel]


class RoomPhotoViewSet(viewsets.ModelViewSet):
    queryset = RoomPhoto.objects.all()
    serializer_class = RoomPhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyHotelRoomRel]
