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
    '''Управление продукцией'''
    permission_classes = [IsAdminOrReadOnly, ]

    def get_object(self, request, format=None):
        if request.user.is_superuser: # если суперпользователь
            return Products.objects.all() # возвращаем весь список
        else: # если пользователь не администратор показать товар который есть в наличии
            return Products.objects.exclude(quantity=0).order_by('art')

    def get(self, request, format=None):
        '''
        description: This API deletes/uninstalls a device.
        parameters:
          - name: name
            type: string
            required: true
            location: form
          - name: bloodgroup
            type: string
            required: true
            location: form
          - name: birthmark
            type: string
            required: true
            location: form
        '''
        products = self.get_object(request)
        serializer = ProductsSerializer(products, many=True)
        return Response(list(serializer.data))

    def post(self, request, format=None):
        '''Добавить продукцию'''
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(dict(serializer.data), status=status.HTTP_201_CREATED)
        return Response({'success': 0,
                         'expection': serializer._errors,
                         'message': 400}, status=status.HTTP_400_BAD_REQUEST)


class ProductsDetailViewSet(APIView):
    '''Управление определенным продуктом'''
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, art):
        return get_object_or_404(Products, art=art)

    def get(self, request, *args, **kwargs):
        '''
        description: This API deletes/uninstalls a device.
        parameters:
          - name: name
            type: string
            required: true
            location: form
          - name: bloodgroup
            type: string
            required: true
            location: form
          - name: birthmark
            type: string
            required: true
            location: form
        '''
        product = self.get_object(kwargs.get('art'))
        serializer = ProductsSerializer(product)
        return Response(dict(serializer.data))

    def put(self, request, *args, **kwargs):
        '''Изменить продукт'''
        product = Products.objects.get(art=kwargs.get('art'))
        serializer = ProductsSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(dict(serializer.data), status=status.HTTP_201_CREATED)
        return Response({'success': 0,
                         'expection': serializer._errors,
                         'message': 400}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        '''Удалить продукт'''
        user = self.get_object(kwargs.get('art'))
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



