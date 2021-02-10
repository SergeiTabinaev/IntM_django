from django.urls import path
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, CartViewSet, CartProductViewSet, AddToCartViewSet

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')


urlpatterns = [
    path('cart/', CartViewSet.as_view({
        'get': 'list',
    })),
    path('cart/<str:pk>', CartViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy'
    })),
    path('cart/cartproducts/', CartProductViewSet.as_view({
        'get': 'list',
    })),
    path('cart/cartproducts/<str:pk>', CartProductViewSet.as_view({
        'get': 'retrieve',
        # 'put': 'update',
        'delete': 'destroy'
    })),
    path('add-to-cart/<str:slug>', AddToCartViewSet.as_view({
        'get': 'retrieve'
    })),

]
urlpatterns += router.urls
