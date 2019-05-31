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
    user_id = SerializerMethodField(read_only=True)
    password = CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('user_id', 'address', 'fio', 'password')

    def get_user_id(self, obj):
        return str(obj.id)

    def create(self, validated_data):
        '''создание пользователя'''
        modifed_validated_data = {
            'address': validated_data.get('address', None),
            'username': validated_data.get('address', None),
            'fio': validated_data.get('fio', None),
            'password': validated_data.get('password', None)
        }
        try:
            user = User.objects.create_user(**modifed_validated_data)
            Basket.objects.create(user_id=user)
        except Exception as e:
            print(str(e))
            raise ValidationError({'address': [str(e).split(':')[0], ]})
        return user

    def update(self, instance, validated_data):
        '''обновление пользователя'''
        instance.address = validated_data.get('address', instance.address),
        instance.username = validated_data.get('address', instance.username),
        instance.fio = validated_data.get('fio', instance.fio),
        if validated_data.get('password', None):
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

# class UsersCreateSerializer(ModelSerializer):
#
#     class Meta:
#         model = get_user_model()
#         fields = ('address', 'fio', 'password')
#
#     def create(self, validated_data):
#         '''создание пользователя'''
#         modifed_validated_data = {
#             'address': validated_data.get('address', None),
#             'username': validated_data.get('address', None),
#             'fio': validated_data.get('fio', None),
#             'password': validated_data.get('password', None)
#         }
#         try:
#             user = get_user_model().objects.create_user(**modifed_validated_data)
#         except Exception as e:
#             print(str(e))
#             raise ValidationError({'address': [str(e).split(':')[0], ]})
#         return user
#
#     def update(self, instance, validated_data):
#         '''обновление пользователя'''
#         instance.address = validated_data.get('address', instance.address),
#         instance.username = validated_data.get('address', instance.username),
#         instance.fio = validated_data.get('fio', instance.fio),
#         if validated_data.get('password', False):
#             instance.set_password(validated_data.get('password'))
#         instance.save()
#         return instance