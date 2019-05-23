from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BasketSerializer

from .models import Basket


class BasketViewSet(APIView):
    queryset = Basket.objects.all().order_by('id')
    serializer_class = BasketSerializer

    def get(self):
        basket = Basket.objects.all()
        serializer = BasketSerializer(basket, many=True)
        return Response(list(serializer))