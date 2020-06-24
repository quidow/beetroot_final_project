from django.contrib import admin
from .models import Amenity, Service, Hotel, HotelAdminRelation, HotelPhoto, Room, RoomPhoto


class RoomPhotoInline(admin.StackedInline):
    model = RoomPhoto
    extra = 0


class RoomAdmin(admin.ModelAdmin):
    filter_horizontal = ('amenities',)
    inlines = [
        RoomPhotoInline,
    ]


# class RoomInline(admin.StackedInline):
#     model = Room
#     extra = 0
#     filter_horizontal = ('amenities',)
#     show_change_link = True
#     # readonly_fields = ('amenities', 'persons',)


class HotelPhotoInline(admin.StackedInline):
    extra = 0
    model = HotelPhoto


class HotelAdmin(admin.ModelAdmin):
    filter_horizontal = ('services',)
    inlines = [
        HotelPhotoInline,
        # RoomInline,
    ]


class HotelAdminRelationAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'admin')


admin.site.register(Amenity)
admin.site.register(Service)
admin.site.register(Room, RoomAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelAdminRelation, HotelAdminRelationAdmin)
