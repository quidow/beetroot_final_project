from rest_framework import viewsets
from .models import Amenity, Service, Hotel, HotelAdminRelation, HotelPhoto, Room, RoomPhoto
from .serializers import AmenitySerializer, ServiceSerializer, HotelSerializer, HotelPhotoSerializer, RoomSerializer, \
    RoomPhotoSerializer
from .permissions import IsAdminOrReadOnly, IsAdminOrReadOnlyHotelRel, IsAdminOrReadOnlyRoomRel, IsSuperUserOrReadOnly


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
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        instance = serializer.save()
        HotelAdminRelation.objects.create(admin=self.request.user, hotel=instance)


class HotelPhotoViewSet(viewsets.ModelViewSet):
    queryset = HotelPhoto.objects.all()
    serializer_class = HotelPhotoSerializer
    permission_classes = [IsAdminOrReadOnlyHotelRel]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminOrReadOnlyHotelRel]


class RoomPhotoViewSet(viewsets.ModelViewSet):
    queryset = RoomPhoto.objects.all()
    serializer_class = RoomPhotoSerializer
    permission_classes = [IsAdminOrReadOnlyRoomRel]
