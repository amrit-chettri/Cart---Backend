from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ProductSerializer, CartSerializer
from .models import Product, Cart

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


@method_decorator(cache_page(60 * 15), name='dispatch')
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
