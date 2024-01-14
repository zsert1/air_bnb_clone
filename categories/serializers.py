from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    # 어떤 필드에 대해서 노출할지 작성
    pk = serializers.IntegerField()
    name = serializers.CharField(required=True)
    kind = serializers.CharField()
    created = serializers.DateTimeField()
