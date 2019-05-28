from django.http import Http404
from django.shortcuts import get_object_or_404
from .serializers import UsersSerializer, UsersCreateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

from .permissions import (
    POSTOrNotForUsers
)

User = get_user_model()


class UserListViewSet(APIView):
    '''Упревление пользователями'''
    permission_classes = [POSTOrNotForUsers, ]

    def get_object(self, request, format=None):
        if request.user.is_superuser: # если суперпользователь
            return User.objects.all() # возвращаем весь список
        else: # если анонимный пользователь, вернет пустой список, если авторизованный: авторизованного пользователя
            return User.objects.filter(id=request.user.id)

    def get(self, request, format=None):
        '''Получить список пользователей'''
        users = self.get_object(request)
        serializer = UsersSerializer(users, many=True)
        return Response(list(serializer.data))

    def post(self, request):
        '''Создать пользователя'''
        serializer = UsersCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = User.objects.get(username=serializer.data['address'])
            return Response({'success': 1,
                             'user_id': user.id,
                             'token_auth': Token.objects.create(user=user).key}, status=status.HTTP_201_CREATED)
        else:
            return Response({'success': 0,
                             'expection': serializer._errors,
                             'message': 400}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailViewSet(APIView):
    '''Управление пользователем'''
    permission_classes = [IsAuthenticated, ]

    def get_object(self, request, pk):
        request_user = request.user
        user = get_object_or_404(User, pk=pk)
        if user == request_user or request_user.is_superuser:
            return user
        else:
            raise Http404

    def get(self, request, pk, format=None):
        '''Получить детализацию по пользователю'''
        user = self.get_object(request, pk)
        serializer = UsersSerializer(user)
        return Response(dict(serializer.data))

    def put(self, request, pk, format=None):
        '''Изменить пользователя'''
        user = self.get_object(request, pk)
        serializer = UsersSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(dict(serializer.data))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        '''Удалить пользователя'''
        user = self.get_object(request, pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
