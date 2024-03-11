from rest_framework.serializers import ModelSerializer
from .models import WishList
from rooms.serializers import RoomListSerializer


class WishListSerializers(ModelSerializer):

    rooms = RoomListSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = WishList
        fields = (
            "name",
            "rooms",
        )
