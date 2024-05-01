from rest_framework import serializers
from .models import Category

# category model 을 json 형태로  어떻게 나타낼지 기술한다.


class CategorySerializer(serializers.Serializer):
    # 카테고리 필드중에 노출한 필드를 지정해준다.
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True,
        max_length=50,
    )
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.kind = validated_data.get("kind", instance.kind)
        instance.save()
        return instance
