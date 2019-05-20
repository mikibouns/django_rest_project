from django.urls import path
from . import views

app_name = 'basket_app'

urlpatterns = [
    path('', views.basket),

]
