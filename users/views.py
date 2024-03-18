from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from . import serializer


class Me(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializers = serializer.PrivateUserSerializer(user).data
        return Response(serializers)

    def put(self, request):
        user = request.user
        serializers = serializer.PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializers.is_valid():
            user = serializers.save()
            serializers = serializer.PrivateUserSerializer(user)
            return Response(serializers.data)

        else:
            Response(serializers.errors)
        pass
