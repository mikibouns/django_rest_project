from .models import Products
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedModelSerializer,
    CharField,
)


class ProductsSerializer(ModelSerializer):

    class Meta:
        model = Products
        fields = ('art', 'name', 'price', 'quantity')
