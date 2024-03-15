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

    def validate(self, data):
        if data["check_out"] <= data["check_in"]:
            raise serializers.ValidationError("퇴실 날짜가 입실 날짜보다 뒤여야 합니다")
        if Booking.objects.filter(
            check_in__gte=data["check_in"],
            check_out__lte=data["check_out"],
        ).exists():
            raise serializers.ValidationError("해당 기간에 이미 예약이 있습니다")
        return data

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guest",
        )
