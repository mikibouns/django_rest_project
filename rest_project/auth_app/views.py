from rest_framework import viewsets, permissions
from django.http import Http404
from .serializers import UsersSerializer, UsersCreateSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes

from django.contrib.auth import get_user_model

from .permissions import (
    POSTOrNotForUsers
)


class UserListViewSet(APIView):
    '''список пользователей'''
    permission_classes = [POSTOrNotForUsers, ]

    def get_object(self, request, format=None):
        if request.user.is_superuser: # если суперпользователь
            return get_user_model().objects.all() # возвращаем весь список
        else:
            return get_user_model().objects.filter(id=request.user.id)

    def get(self, request, format=None):
        users = self.get_object(request)
        serializer = UsersSerializer(users, many=True)
        return Response(list(serializer.data))

    def post(self, request):
        serializer = UsersCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = get_user_model().objects.get(username=serializer.data['address'])
            return Response({'success': 1,
                             'user_id': user.id,
                             'token_auth': Token.objects.create(user=user).key}, status=status.HTTP_201_CREATED)
        else:
            return Response({'success': 0,
                             'expection': serializer._errors,
                             'message': 400}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailViewSet(APIView):
    '''детализация по пользователю'''
    permission_classes = [IsAuthenticated, ]

    def get_object(self, request, pk):
        request_user = request.user
        try:
            user = get_user_model().objects.get(pk=pk)
            if user == request_user or request_user.is_superuser:
                return user
            else:
                raise Http404
        except get_user_model().DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(request, pk)
        serializer = UsersSerializer(user)
        return Response(dict(serializer.data))

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(request, pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)