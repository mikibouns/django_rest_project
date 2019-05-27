from django.urls import path
from . import views

app_name = 'basket_app'

urlpatterns = [
    path('', views.BasketListViewSet.as_view()),
    path('<int:pk>', views.BasketDetailViewSet.as_view()),
]
