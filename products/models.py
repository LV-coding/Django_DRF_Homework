from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta():
        ordering = ('-id',)

    def __str__(self):
        return self.name
