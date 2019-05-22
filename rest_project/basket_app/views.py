from .models import Basket
from rest_framework import viewsets
from .serializers import BasketSerializer


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all().order_by('id')
    serializer_class = BasketSerializer