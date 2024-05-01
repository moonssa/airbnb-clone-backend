from rest_framework import serializers

# category model 을 json 형태로  어떻게 나타낼지 기술한다.


class CategorySerializer(serializers.Serializer):
    # 카테고리 필드중에 노출한 필드를 지정해준다.
    pk = serializers.IntegerField()
    name = serializers.CharField(required=True)
    kind = serializers.CharField()
    created_at = serializers.DateTimeField()
