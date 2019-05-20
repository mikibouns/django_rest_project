from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    CharField
)


class UsersListSerializer(ModelSerializer):
    user_id = SerializerMethodField()
    user_address = SerializerMethodField()
    user_fio = SerializerMethodField()

    class Meta:
        model = get_user_model()
        field = ('user_id', 'user_address', 'user_fio')

    def get_user_id(self, obj):
        return int(obj.id)

    def get_user_fio(self, obj):
        return str(obj.fio)

    def get_user_address(self, obj):
        return str(obj.address)


class UsersCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        field = ('username', 'email', 'password', 'is_staff')

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data.get('email', None)
        is_staff = validated_data.get('is_staff', False)
        user = get_user_model().objects.create_user(username=username, email=email, is_staff=is_staff)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        if validated_data.get('password', False):
            instance.set_password(validated_data['password'])
        instance.save()
        return instance