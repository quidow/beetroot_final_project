from rest_framework import routers
from .views import AmenityViewSet, ServiceViewSet, HotelViewSet, HotelPhotoViewSet, RoomViewSet, RoomPhotoViewSet


router = routers.DefaultRouter()
router.register(r'amenities', AmenityViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'hotels-photos', HotelPhotoViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'rooms-photos', RoomPhotoViewSet)
