from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from products.models import Product
from orders.models import Order
from .serializer import ProductSerializer, OrderSerializer


class ProductListViewSet(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_scope = 'products'
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
        ]
    filterset_fields = '__all__'
    search_fields = ['=name']
    ordering_fields = '__all__'


class ProductViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_scope = 'product'


class OrderListViewSet(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_scope = 'orders'
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
        ]
    filterset_fields = '__all__'
    search_fields = ['product__name']
    ordering_fields = '__all__'


class OrderViewSet(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_scope = 'order'
