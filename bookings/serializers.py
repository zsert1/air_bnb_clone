from rest_framework import serializers
from .models import Booking
from django.utils import timezone


class PublicBookingSerializers(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guest",
        )


class CreateRoomSerializers(serializers.ModelSerializer):
    check_in = serializers.DateField()
    check_out = serializers.DateField()

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("현재보다 과거는 예약이 안됩니다.")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("현재보다 과거는 예약이 안됩니다.")
        return value

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guest",
        )
