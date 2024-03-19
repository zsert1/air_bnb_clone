from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from . import serializers


class Me(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializers = serializers.PrivateUserSerializer(user).data
        return Response(serializers)

    def put(self, request):
        user = request.user
        serializers = serializers.PrivateUserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializers.is_valid():
            user = serializers.save()
            serializers = serializers.PrivateUserSerializer(user)
            return Response(serializers.data)
        else:
            Response(serializers.errors)
        pass


class Users(APIView):
    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError
        serializer = serializers.PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = serializers.PrivateUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
