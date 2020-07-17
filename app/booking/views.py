from rest_framework import permissions, status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.response import Response

from django.db import connection

from .models import Amenity, Service, Hotel, HotelPhoto, Room, RoomPhoto, RoomPrice
from .permissions import IsOwnerOrReadOnly, IsSuperUserOrReadOnly, IsOwnerOrReadOnlyHotelRel, \
    IsOwnerOrReadOnlyHotelRoomRel
from .serializers import AmenitySerializer, ServiceSerializer, HotelReadSerializer, HotelWriteSerializer, \
    HotelPhotoSerializer, \
    RoomPhotoSerializer, RoomReadSerializer, RoomWriteSerializer, RoomPriceSerializer


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyHotelRel]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return RoomReadSerializer
        return RoomWriteSerializer

    def perform_create(self, serializer):
        hotel = Hotel.objects.get(pk=self.get_parents_query_dict()['hotel'])
        serializer.save(hotel=hotel)

    @action(detail=True, methods=['get'])
    def calculate_price(self, request, parent_lookup_hotel, pk=None):
        if not Room.objects.filter(pk=pk).exists():
            return Response(f"Room with id {pk} does not exist.", status=status.HTTP_404_NOT_FOUND)
        with connection.cursor() as cursor:
            try:
                cursor.execute(f"""SELECT SUM(price)
                    FROM
                      (SELECT "date",
                              first_value(price) OVER (PARTITION BY price_partition
                                                       ORDER BY "date") AS price
                       FROM
                         (SELECT p."date",
                                 p.price,
                                 sum(CASE
                                         WHEN p.price IS NULL THEN 0
                                         ELSE 1
                                     END) OVER (
                                                ORDER BY p."date") AS price_partition
                          FROM
                            (SELECT x."date",
                                    t.price
                             FROM
                               (SELECT generate_series(min("date"), '{request.query_params['check_out']}'::date, '1 day')::date AS "date"
                                FROM public.booking_roomprice
                                where room_id = {pk}) x
                             LEFT   JOIN (select * from public.booking_roomprice where room_id = {pk}) t USING ("date")
                             ORDER  BY x."date") AS p
                          ORDER  BY p."date") AS q) AS z
                    WHERE "date" >= '{request.query_params['check_in']}'::date""")
                row = cursor.fetchone()
            except:
                return Response("Something is wrong!", status=status.HTTP_400_BAD_REQUEST)
        return Response({"price": row[0]})


class RoomPriceViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = RoomPrice.objects.all()
    serializer_class = RoomPriceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyHotelRoomRel]

    def perform_create(self, serializer):
        room = Room.objects.get(pk=self.get_parents_query_dict()['room'])
        serializer.save(room=room)


class RoomPhotoViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = RoomPhoto.objects.all()
    serializer_class = RoomPhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyHotelRoomRel]

    def perform_create(self, serializer):
        room = Room.objects.get(pk=self.get_parents_query_dict()['room'])
        serializer.save(room=room)
