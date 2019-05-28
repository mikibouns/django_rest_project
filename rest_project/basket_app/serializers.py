from .models import Basket, ProductList
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    HyperlinkedModelSerializer,
)


class ProductListSerializer(ModelSerializer):
    product_name = SerializerMethodField()
    product_art = SerializerMethodField()

    class Meta:
        model = ProductList
        fields = ('id', 'product_name', 'product_art', 'quantity')

    def get_product_name(self, obj):
        return str(obj.product.name)

    def get_product_art(self, obj):
        return str(obj.product.art)


class UpdateBasketSerializer(ModelSerializer):

    class Meta:
        model = ProductList
        fields = ('id', 'quantity')

    def update(self, instance, validated_data):
        print(validated_data)
        return instance



class BasketSerializer(ModelSerializer):
    products = SerializerMethodField()
    basket_id = SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('basket_id', 'user_id', 'products')

    def get_products(self, obj):
        data = ProductListSerializer(obj.product_children(), many=True).data
        if data:
            return data
        return None

    def get_basket_id(self, obj):
        return obj.id


class AddToBasketSerializer(ModelSerializer):

    class Meta:
        model = ProductList
        fields = ('product', 'quantity')

    def create(self, validated_data):
        validated_data['basket'] = self.context.get('basket')
        try:
            ProductList.objects.get(product=validated_data.get('product'))
            raise ValidationError({'product': ['product {} already exists in the basket'.format(validated_data.get('product').art)]})
        except ProductList.DoesNotExist:
            if ProductList.quantity_calculation(product=validated_data.get('product'), quantity=abs(validated_data.get('quantity', 1))):
                purchase = ProductList.objects.create(**validated_data)
                return purchase
            raise ValidationError({'quantity': 'not enough products in stock, check product availability'})
