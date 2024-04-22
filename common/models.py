from django.db import models


# Create your models here.
class CommonModel(models.Model):
    """다른 필드에서 재사용 하려는 모델"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
