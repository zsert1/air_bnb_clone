from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import WishList
from .serializers import WishListSerializers
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_200_OK
from rooms.models import Room


class WishLists(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_wishlist = WishList.objects.filter(user=request.user)
        serializer = WishListSerializers(
            all_wishlist,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = WishListSerializers(data=request.data)
        if serializer.is_valid():
            wishlist = serializer.save(
                user=request.user,
            )
            serializer = WishListSerializers(wishlist)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WishlistDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return WishList.objects.get(pk=pk, user=user)
        except WishList.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        wishlist = self.get_object(pk, request.user)
        serializers = WishListSerializers(
            wishlist,
            context={"request": request},
        )
        return Response(serializers.data)

    def delete(self, request, pk):
        wishlist = self.get_object(pk, request.user)
        wishlist.delete()
        return Response(status=HTTP_200_OK)

    def put(self, request, pk):
        wishlist = self.get_object(pk, request.user)
        serializers = WishListSerializers(
            wishlist,
            data=request.data,
            partial=True,
        )
        if serializers.is_valid():
            wishlist = serializers.save()
            serializers = WishListSerializers(wishlist)
            return Response(serializers.data)
        else:
            return Response(serializers.errors)


class WishlistToggle(APIView):
    def get_list(self, pk, user):
        try:
            return WishList.objects.get(pk=pk, user=user)
        except WishList.DoesNotExist:
            raise NotFound

    def get_room(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def put(self, request, pk, room_pk):
        wishlist = self.get_list(pk, request.user)
        room = self.get_room(room_pk)
        if wishlist.rooms.filter(pk=room.pk).exists():
            wishlist.rooms.remove(room)
        else:
            wishlist.rooms.add(room)
        return Response(status=HTTP_200_OK)
