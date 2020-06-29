from rest_framework import permissions

from .models import Hotel, Room


class IsSuperUserOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        return request.user in obj.owners.all()


class IsOwnerOrReadOnlyHotelRel(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        if request.method == 'POST' and request.data:
            hotel = Hotel.objects.get(pk=request.data["hotel"])
            return request.user in hotel.owners.all()

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        return request.user in obj.hotel.owners.all()


class IsOwnerOrReadOnlyHotelRoomRel(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        if request.method == 'POST' and request.data:
            room = Room.objects.get(pk=request.data["room"])
            return request.user in room.hotel.owners.all()

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser:
            return True

        return request.user in obj.room.hotel.owners.all()
