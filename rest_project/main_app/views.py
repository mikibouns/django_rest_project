from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRootView(APIView):

    def get(self, request):
        data = [
            {
                'api_url': request.build_absolute_uri(),
                'method': 'get',
                'comments': 'Доступные url (этот документ)'
            },
            {
                'api_url': reverse('auth:user_list', request=request),
                'method': 'get',
                'comments': 'Список пользователей'
            },
            {
                'api_url': reverse('auth:user_detail', args=[1], request=request),
                'method': 'get',
                'comments': 'Получить пользователя c id=1'
            },
            {
                'api_url': reverse('product:product_list', request=request),
                'method': 'get',
                'comments': 'Список продуктов'
            },
            {
                'api_url': reverse('product:product_detail', args=[111111], request=request),
                'method': 'get',
                'comments': 'Получить продукт c art=111111'
            },
            {
                'api_url': reverse('basket:basket_list', request=request),
                'method': 'get',
                'comments': 'Список корзин пользователей и их содержимое'
            },
            {
                'api_url': reverse('basket:basket_detail', args=[1], request=request),
                'method': 'get',
                'comments': 'Получить корзину c id=1'
            },
        ]
        return Response(data)