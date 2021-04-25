from django.urls import path, include
from shop.views import ProductViewSet, CartViewSet, CartItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('carts', CartViewSet)
router.register('cart_items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]