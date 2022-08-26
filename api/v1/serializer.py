from rest_framework import serializers
from products.models import Product
from orders.models import Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = ('name', 'description', 'price', 'created_at')


class OrderSerializer(serializers.ModelSerializer):
    class Meta():
        model = Order
        fields = ('product', 'created_at')