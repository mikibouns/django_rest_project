from django.db import models
from product_app.models import Products
from django.contrib.auth import get_user_model


class Basket(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='user')
    product_list = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='product_list')
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id)