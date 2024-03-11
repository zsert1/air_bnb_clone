from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import WishList
from .serializers import WishListSerializers


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


# Create your views here.
