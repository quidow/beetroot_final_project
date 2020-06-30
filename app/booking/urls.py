from rest_framework import routers
from .views import AmenityViewSet, ServiceViewSet, HotelViewSet, HotelPhotoViewSet, RoomViewSet, RoomPhotoViewSet
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, routers.SimpleRouter):
    pass


router = NestedDefaultRouter()
router.register(r'amenities', AmenityViewSet)
router.register(r'services', ServiceViewSet)
hotels = router.register(r'hotels', HotelViewSet)
hotels.register(
    'photos', HotelPhotoViewSet,
    basename='hotels-photos',
    parents_query_lookups=['hotel']
)
hotels.register(
    r'rooms', RoomViewSet,
    basename='hotels-rooms',
    parents_query_lookups=['hotel']
).register(
    r'photos', RoomPhotoViewSet,
    basename='rooms-photos',
    parents_query_lookups=['room__hotel', 'room']
)
