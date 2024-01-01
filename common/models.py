from django.db import models


# 재사용을 위한 모델
class CommonModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta는 장고에서 모델을 configure할 때 사용
    class Meta:
        abstract = True
