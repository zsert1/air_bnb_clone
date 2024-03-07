from rest_framework import serializers
from .models import Review
from users.serializer import TinyUserSerializer


class ReviewSerialzers(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = (
            "user",
            "payload",
            "rating",
        )
