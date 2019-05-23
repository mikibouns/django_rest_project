from django.contrib.auth import get_user_model
from basket_app.models import Basket
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedModelSerializer,
    CharField
)


class UsersSerializer(ModelSerializer):
    user_id = SerializerMethodField()
    address = SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('user_id', 'address', 'fio')

    def get_user_id(self, obj):
        return str(obj.id)

    def get_address(self, obj):
        return str(obj.email)


class UsersCreateSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'fio')

    def create(self, validated_data):
        print(validated_data)
        user = get_user_model().objects.create_user(**validated_data)
        return user
