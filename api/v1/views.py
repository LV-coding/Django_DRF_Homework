from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from products.models import Product
from orders.models import Order
from .serializer import ProductSerializer, OrderSerializer


class ProductListViewSet(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderListViewSet(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderViewSet(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
