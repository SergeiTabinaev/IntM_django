from django.urls import path
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, CartViewSet, CartProductViewSet, AddToCartViewSet

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')  # категории товаров
router.register('product', ProductViewSet, basename='product')     # товары


urlpatterns = [
    path('cart/', CartViewSet.as_view({   # список корзин(всех пользователей)
        'get': 'list',
    })),
    path('cart/<str:pk>', CartViewSet.as_view({  # список корзины конкретного пользователя
        'get': 'retrieve',
    })),
    path('cart/cartproducts/', CartProductViewSet.as_view({   # cписок всех продуктов в корзине
        'get': 'list',
    })),
    path('cart/cartproducts/<str:pk>', CartProductViewSet.as_view({  # удаление продукта из корзины
        'get': 'retrieve',
        # 'put': 'update',
        'delete': 'destroy'
    })),
    path('add-to-cart/<str:slug>', AddToCartViewSet.as_view(), name='add-to-cart')  # добавление товара в корзину
]

urlpatterns += router.urls
