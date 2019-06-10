from django.contrib import admin

from airbnb.rooms.models import Room, RoomPhoto, Amenity, Review


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display_links = (
        'id',
    )

    search_fields = (
        'city',
        'location',
    )

    list_filter = (
        'price',
        'capacity_cnt',
    )

    list_display = (
        'id',
        'host',
        'city',
        'location',
        'name',
        'price',
        'capacity_cnt',

    )


@admin.register(RoomPhoto)
class RoomPhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'room',
        'photo',
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'key',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'room',
        'creator',
        'message',
        'rating',
    )
