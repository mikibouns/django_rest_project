from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=256, unique=True)
    price = models.DecimalField(max_digits=10, default=0, decimal_places=2)
    art = models.PositiveIntegerField(unique=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.art)