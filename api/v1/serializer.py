from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from products.models import Product
from orders.models import Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = ('name', 'description', 'price', 'created_at')
        validators = [
            UniqueTogetherValidator(
                queryset = Product.objects.all(),
                fields = ['name', 'description', 'price'],
                message = "The fields name, description, price must make a unique set. Please, check your product..."
            )
        ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta():
        model = Order
        fields = ('product', 'created_at')
