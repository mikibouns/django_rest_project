from django.contrib.auth import get_user_model
from basket_app.models import Basket
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    CharField
)

User = get_user_model()


class UsersSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'address', 'fio', 'password')


class UsersCreateUpdateSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'address', 'fio', 'password')

    def create(self, validated_data):
        '''создание пользователя'''
        print(validated_data)
        modifed_validated_data = {
            'address': validated_data.get('address', None),
            'username': validated_data.get('address', None),
            'fio': validated_data.get('fio', None),
            'password': validated_data.get('password', None)
        }
        try:
            user = get_user_model().objects.create_user(**modifed_validated_data)
        except Exception as e:
            print(str(e))
            raise ValidationError({'address': [str(e).split(':')[0], ]})
        return user

    def update(self, instance, validated_data):
        '''обновление пользователя'''
        user_addr = validated_data.get('address', instance.address)
        instance.fio = validated_data.get('fio', instance.fio)
        instance.address = user_addr
        instance.username = user_addr
        if validated_data.get('password', False):
            instance.set_password(validated_data['password'])
        instance.save()
        return instance