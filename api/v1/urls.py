from django.urls import path, include
from .views import ProductViewSet, ProductListViewSet, OrderListViewSet, OrderViewSet


urlpatterns = [
    path("products", ProductListViewSet.as_view()),
    path("orders", OrderListViewSet.as_view()),
    path("product/<int:pk>", ProductViewSet.as_view()),
    path("order/<int:pk>", OrderViewSet.as_view()),
]
