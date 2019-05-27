from django.urls import path
from . import views

app_name = 'product_app'

urlpatterns = [
    path('', views.ProductsListViewSet.as_view(), name='products'),
    path('<int:art>', views.ProductsDetailViewSet.as_view(), name='product'),
    # path('<int:art>/add', views.AddToBasketViewSet.as_view(), name='product_add')
]
