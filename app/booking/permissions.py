from rest_framework import permissions
from .models import HotelAdminRelation, Room


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return HotelAdminRelation.objects.filter(admin=request.user, hotel=obj).exists()


class IsAdminOrReadOnlyHotelRel(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'POST' and request.user.is_authenticated and request.data:
            return HotelAdminRelation.objects.filter(admin=request.user, hotel=request.data.get("hotel", None)).exists()

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return HotelAdminRelation.objects.filter(admin=request.user, hotel=obj.hotel).exists()


class IsAdminOrReadOnlyRoomRel(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'POST' and request.user.is_authenticated and request.data:
            room = Room.objects.get(pk=request.data.get("room", None))
            return HotelAdminRelation.objects.filter(admin=request.user, hotel=room.hotel).exists()

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return HotelAdminRelation.objects.filter(admin=request.user, hotel=obj.room.hotel).exists()
