from .models import Products
from rest_framework import viewsets
from .serializers import ProductsSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all().order_by('name')
    serializer_class = ProductsSerializer