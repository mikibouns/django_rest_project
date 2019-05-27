from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Basket
from .serializers import BasketSerializer, AddToBasketSerializer


class BasketListViewSet(APIView):
    '''список корзин пользователя'''
    permission_classes = [IsAuthenticated, ]

    def get_object(self, *args, **kwargs):
        if self.request.user.is_superuser: # если суперпользователь
            return Basket.objects.all() # возвращаем весь список
        else: # если авторизованный: вернет корзины авторизованного пользователя
            return Basket.objects.filter(user_id=self.request.user)

    def get(self, request, *args, **kwargs):
        basket = self.get_object(request)
        serializer = BasketSerializer(basket, many=True)
        return Response(list(serializer.data))

    def post(self, *args, **kwargs):
        print(self.request.data)
        serializer = AddToBasketSerializer(data=self.request.data, context={'user_id': self.request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(dict(serializer.data), status=status.HTTP_201_CREATED)
        return Response({'success': 0,
                         'expection': serializer._errors,
                         'message': 400}, status=status.HTTP_400_BAD_REQUEST)



class BasketDetailViewSet(APIView):
    '''информация по корзине'''
    permission_classes = [IsAuthenticated, ]

    def get_object(self, *args, **kwargs):
        request_user = self.request.user
        basket = get_object_or_404(Basket, pk=kwargs.get('pk'))
        if basket.user_id == request_user or request_user.is_superuser:
            return basket
        else:
            raise Http404

    def get(self, request, *args, **kwargs):
        basket = self.get_object(kwargs.get('pk'))
        serializer = BasketSerializer(basket)
        return Response(dict(serializer.data))

    def delete(self, request, *args, **kwargs):
        basket = self.get_object(kwargs.get('pk'))
        basket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


