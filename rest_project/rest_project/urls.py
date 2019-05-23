"""rest_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as auth_token

from rest_framework.schemas import get_schema_view
from rest_framework import routers
from auth_app import views as auth_views
from product_app import views as products_views
from basket_app import views as basket_views


# schema_view = get_schema_view(title='Django-api-project')
#
#
# router = routers.DefaultRouter()
# router.register(r'users', auth_views.UserViewSet)
# router.register(r'products', products_views.ProductsViewSet)
# router.register(r'basket', basket_views.BasketViewSet)

urlpatterns = [
    # path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    # path('schema/', schema_view, name='schema'),

    path('api-token-auth/', auth_token.obtain_auth_token, name='token_auth'),

    path('api/v1/users/', include('auth_app.urls', namespace='auth')),
    path('api/v1/products/', include('product_app.urls', namespace='product')),
    path('api/v1/basket/', include('basket_app.urls', namespace='basket')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)