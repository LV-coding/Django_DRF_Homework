from rest_framework import serializers
from products.models import Product
from orders.models import Order
from rest_framework.validators import UniqueTogetherValidator


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
