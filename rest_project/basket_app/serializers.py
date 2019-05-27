from .models import Basket
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedModelSerializer,
    CharField
)


class BasketSerializer(ModelSerializer):
    product = SerializerMethodField()
    basket_id = SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('basket_id', 'user_id', 'product', 'quantity')

    def get_basket_id(self, obj):
        return obj.id

    def get_product(self, obj):
        return str(obj.product.name)


class AddToBasketSerializer(ModelSerializer):

    class Meta:
        model = Basket
        fields = ('product', 'quantity')

    def create(self, validated_data):
        print(validated_data)
        purchase = Basket(**validated_data)
        purchase.save()
        return purchase

    def get_user(self, obj):
        return str(obj.request.user.id)
