from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Sta all prices to zero")
def resetPrices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (resetPrices,)

    list_display = [
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created",
    ]

    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "pet_friendly",
        "kind",
        "amenities",
        "created",
        "updated",
    )
    search_fields = (
        "^name",
        "^price",
        "owner__username",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created",
        "updated",
    )

    readonly_fields = (
        "created",
        "updated",
    )
