from .models import Products
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedModelSerializer,
    CharField
)


class ProductsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ('art', 'name', 'price')