from django.urls import path
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, CartViewSet, CartProductViewSet


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
        'delete': 'destroy'
    })),

]
urlpatterns += router.urls
