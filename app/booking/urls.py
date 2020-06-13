from rest_framework import routers
from .views import AmenityViewSet, ServiceViewSet, HotelViewSet, RoomViewSet


router = routers.DefaultRouter()
router.register(r'amenities', AmenityViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
