from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # 원하는 것만 보여줄 떄
        # fields = (
        #     "name",
        #     "kind",
        # )
        # 모든것 보여줄때
        fields = (
            "name",
            "kind",
        )
        #  보여지지  않을것
        # exclude = ("created",)
