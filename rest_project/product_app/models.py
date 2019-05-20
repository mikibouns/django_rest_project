from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=2, default=0, max_length=10)
    art = models.PositiveIntegerField(unique=True)
