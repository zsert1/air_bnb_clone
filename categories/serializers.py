from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    # 어떤 필드에 대해서 노출할지 작성
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.ChoiceField(
        choices=Category.CategotyKindCHoices.choices,
    )
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
