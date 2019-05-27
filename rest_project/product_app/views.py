from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
# from rest_framework.permissions import IsAuthenticated

from .serializers import ProductsSerializer
from .models import Products
from .permissions import (
    IsAdminOrReadOnly
)


class ProductsListViewSet(APIView):
    '''список продукции'''
    permission_classes = [IsAdminOrReadOnly, ]

    def get_object(self, request, format=None):
        if request.user.is_superuser: # если суперпользователь
            return Products.objects.all() # возвращаем весь список
        else: # если пользователь не администратор показать товар который есть в наличии
            return Products.objects.exclude(quantity=0).order_by('id')

    def get(self, request, format=None):
        products = self.get_object(request)
        serializer = ProductsSerializer(products, many=True)
        return Response(list(serializer.data))

    def post(self, request, format=None):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(dict(serializer.data), status=status.HTTP_201_CREATED)
        return Response({'success': 0,
                         'expection': serializer._errors,
                         'message': 400}, status=status.HTTP_400_BAD_REQUEST)


class ProductsDetailViewSet(APIView):
    '''управление списком продукции, для обычных пользователей только чтение'''
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, art):
        return get_object_or_404(Products, art=art)

    def get(self, request, *args, **kwargs):
        product = self.get_object(kwargs.get('art'))
        serializer = ProductsSerializer(product)
        return Response(dict(serializer.data))

    def put(self, request, *args, **kwargs):
        product = Products.objects.get(art=kwargs.get('art'))
        serializer = ProductsSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(dict(serializer.data), status=status.HTTP_201_CREATED)
        return Response({'success': 0,
                         'expection': serializer._errors,
                         'message': 400}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = self.get_object(kwargs.get('art'))
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



