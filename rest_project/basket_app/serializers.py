from .models import Basket
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedModelSerializer,
    CharField
)


class BasketSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Basket
        fields = ('user_id', 'product_list')



