from django.contrib import admin
from .models import Basket


class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'product_list')

admin.site.register(Basket, BasketAdmin)
