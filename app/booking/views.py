from rest_framework import permissions
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Amenity, Service, Hotel, HotelPhoto, Room, RoomPhoto
from .permissions import IsOwnerOrReadOnly, IsSuperUserOrReadOnly, IsOwnerOrReadOnlyHotelRel, \
    IsOwnerOrReadOnlyHotelRoomRel
from .serializers import AmenitySerializer, ServiceSerializer, HotelReadSerializer, HotelWriteSerializer, \
    HotelPhotoSerializer, \
    RoomPhotoSerializer, RoomReadSerializer, RoomWriteSerializer


class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [IsSuperUserOrReadOnly]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsSuperUserOrReadOnly]


class HotelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    # serializer_class = HotelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # @action(detail=True, methods=['get', 'post', 'delete'])
    # def photos(self, request, pk=None):
    #     print(pk)
    #     if request.method == 'GET':
    #         hotel = self.get_object()
    #         photos = HotelPhoto.objects.filter(hotel=hotel)
    #         print(len(photos))
    #         serializer = HotelPhotoSerializer(data=photos, many=True, context={'request': request})
    #         serializer.is_valid()
    #         return Response(serializer.data)
    #     if request.method == 'POST':
    #         hotel = self.get_object()
    #         photo = HotelPhoto.objects.create(hotel=hotel, photo=request.data["photo"])
    #         serializer = HotelPhotoSerializer(photo)
    #         return Response(serializer.data)
    #     if request.method == 'DELETE':
    #         HotelPhoto.objects.get(pk=pk).delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return HotelReadSerializer
        return HotelWriteSerializer

    def perform_create(self, serializer):
        serializer.save(owners=[self.request.user])


class HotelPhotoViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = HotelPhoto.objects.all()
    serializer_class = HotelPhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyHotelRel]

    def perform_create(self, serializer):
        hotel = Hotel.objects.get(pk=self.get_parents_query_dict()['hotel'])
        serializer.save(hotel=hotel)


class RoomViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Room.objects.all()
    # serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyHotelRel]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return RoomReadSerializer
        return RoomWriteSerializer


class RoomPhotoViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = RoomPhoto.objects.all()
    serializer_class = RoomPhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyHotelRoomRel]

    def perform_create(self, serializer):
        room = Room.objects.get(pk=self.get_parents_query_dict()['room'])
        serializer.save(room=room)
