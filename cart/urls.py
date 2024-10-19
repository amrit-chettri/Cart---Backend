
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet , CartViewSet
from .import views

router = DefaultRouter()
router.register(r'products', ProductViewSet )    
router.register(r'cart', CartViewSet) 
   


urlpatterns = [
    path('', include(router.urls)),  
]
