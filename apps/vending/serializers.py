from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=4, decimal_places=2)
    stock = serializers.DecimalField(max_digits=5, decimal_places=0)
    logo = serializers.URLField(max_length=200)
    color = serializers.CharField(max_length=7, default="#ffffff")


class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    balance = serializers.DecimalField(max_digits=4, decimal_places=2)

    def get_user(self, instance):
        return instance