from django.contrib.auth import get_user_model
from basket_app.models import Basket
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedModelSerializer,
    CharField,
    EmailField,
    ValidationError
)


class UsersSerializer(ModelSerializer):
    user_id = SerializerMethodField()

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
        fields = ('address', 'fio', 'password')

    def create(self, validated_data):
        modifed_validated_data = {
            'address': validated_data['address'],
            'username': validated_data['address'],
            'fio': validated_data['fio'],
            'password': validated_data['password']
        }
        try:
            user = get_user_model().objects.create_user(**modifed_validated_data)
        except Exception as e:
            print(str(e))
            raise ValidationError({'address': [str(e).split(':')[0], ]})
        return user
