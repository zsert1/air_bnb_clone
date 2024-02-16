from rest_framework import serializers
from .models import Review


class ReviewSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
