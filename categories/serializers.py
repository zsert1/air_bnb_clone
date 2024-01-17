from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    # 어떤 필드에 대해서 노출할지 작성
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.CharField(
        max_length=15,
    )
    created = serializers.DateTimeField(read_only=True)
