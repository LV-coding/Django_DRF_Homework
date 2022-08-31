from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from products.models import Product
from orders.models import Order
from .serializer import ProductSerializer, OrderSerializer
from api.tasks import user_record
from datetime import datetime


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

    def get(self, request, *args, **kwargs):

        user_agent = request.META['HTTP_USER_AGENT']
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        user_record.delay(user_agent, ip, datetime.now(), 'product_list')
        return self.list(request, *args, **kwargs)



class ProductViewSet(RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_scope = 'product'

    def retrieve(self, request, *args, **kwargs):
        
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        user_agent = request.META['HTTP_USER_AGENT']
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        user_record.delay(user_agent, ip, datetime.now(), f'product_id_{instance.pk}')
        return Response(serializer.data)



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

    def get(self, request, *args, **kwargs):
    
        user_agent = request.META['HTTP_USER_AGENT']
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        user_record.delay(user_agent, ip, datetime.now(), 'order_list')
        return self.list(request, *args, **kwargs)



class OrderViewSet(RetrieveAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_scope = 'order'

    def retrieve(self, request, *args, **kwargs):
        
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        user_agent = request.META['HTTP_USER_AGENT']
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        user_record.delay(user_agent, ip, datetime.now(), f'order_id_{instance.pk}')
        return Response(serializer.data)

