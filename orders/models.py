from django.db import models
from products.models import Product
from django.utils import timezone


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta():
        ordering = ('-id',)

    def __str__(self):
        return f'Order for {self.product}'
    

