from rest_framework.views import APIView
from .serializers import PerkSerializer
from .models import Perk
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT


class Perks(APIView):

    def get(self, request):
        all_perks = Perk.objects.all()
        serializer = PerkSerializer(
            all_perks,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PerkSerializer(data=request.data)
        if serializer.is_valid():
            perk = serializer.save()
            return Response(
                PerkSerializer(perk).data,
            )
        else:
            return Response(PerkSerializer.errors)


class PerkDetail(APIView):
    def get_perk(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except Perk.DoesNotExist:
            return NotFound

    def get(self, request, pk):
        perk = self.get_perk(pk)
        serializer = PerkSerializer(perk)
        return Response(serializer.data)

    def put(self, request, pk):
        perk = self.get_perk(pk)
        serializer = PerkSerializer(
            perk,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            update_perk = serializer.save()
            return Response(
                PerkSerializer(update_perk).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        perk = self.get_perk(pk)
        perk.delete()
        return Response(status=HTTP_204_NO_CONTENT)
