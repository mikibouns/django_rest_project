from django.contrib import admin
from .models import Basket


class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'product', 'quantity')


admin.site.register(Basket, BasketAdmin)