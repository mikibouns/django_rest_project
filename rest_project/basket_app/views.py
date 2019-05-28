from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Basket, ProductList
from .serializers import BasketSerializer, AddToBasketSerializer, ProductListSerializer, UpdateBasketSerializer


class BasketListViewSet(APIView):
    '''список корзин пользователей'''
    permission_classes = [IsAuthenticated, ]

    def get_object(self, *args, **kwargs):
        if self.request.user.is_superuser: # если суперпользователь
            return Basket.objects.all() # возвращаем весь список
        else: # если авторизованный пользователь: вернет корзину авторизованного пользователя
            return Basket.objects.filter(user_id=self.request.user)

    def get(self, request, *args, **kwargs):
        basket = self.get_object(request)
        serializer = BasketSerializer(basket, many=True)
        return Response(list(serializer.data))

    def post(self, *args, **kwargs):
        try:
            basket = Basket.objects.get(user_id=self.request.user)
        except Basket.DoesNotExist:
            basket = Basket.objects.create(user_id=self.request.user)

        serializer = AddToBasketSerializer(data=self.request.data, context={'basket': basket})
        if serializer.is_valid():
            serializer.save()
            return Response(dict(serializer.data), status=status.HTTP_201_CREATED)
        return Response({'success': 0,
                         'expection': serializer._errors,
                         'message': 400}, status=status.HTTP_400_BAD_REQUEST)


class BasketDetailViewSet(APIView):
    '''корзине определенного пользователя'''
    permission_classes = [IsAuthenticated, ]

    def get_object(self, pk):
        request_user = self.request.user
        basket = get_object_or_404(Basket, pk=pk)
        if basket.user_id == request_user or request_user.is_superuser:
            return basket
        else:
            raise Http404

    def get(self, request, *args, **kwargs):
        basket = self.get_object(kwargs.get('pk'))
        serializer = ProductListSerializer(ProductList.objects.filter(basket=basket), many=True)
        return Response(list(serializer.data))

    def put(self, *args, **kwargs):
        if self.request.data.get('id', None):
            basket = self.get_object(kwargs.get('pk'))
            try:
                instance = ProductList.objects.filter(basket=basket).get(id=self.request.data.get('id'))
            except ProductList.DoesNotExist:
                return Response({'success': 0,
                                 'expection': 'product id={} does not exist'.format(self.request.data['id']),
                                 'message': 400}, status=status.HTTP_400_BAD_REQUEST)
            serialiser = UpdateBasketSerializer(instance, self.request.data, partial=True)
            if serialiser.is_valid():
                serialiser.save()
                return Response(dict(serialiser.data))
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, *args, **kwargs):
        basket = self.get_object(kwargs.get('pk'))
        if self.request.data.get('id', None):
            try:
                purchase = ProductList.objects.filter(basket=basket).get(id=self.request.data.get('id'))
                ProductList.quantity_calculation(product=purchase.product,
                                                 quantity=purchase.quantity * -1)
                purchase.delete()
                return Response(status=status.HTTP_200_OK)
            except ProductList.DoesNotExist:
                return Response({'success': 0,
                                 'expection': 'product id={} does not exist'.format(self.request.data['id']),
                                 'message': 400}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


