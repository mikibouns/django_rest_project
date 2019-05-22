from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, default=0, decimal_places=2)
    art = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return str(self.name)