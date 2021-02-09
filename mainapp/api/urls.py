from django.urls import path
from rest_framework import routers
from .views import CategoryViewSet, ProductViewSet, CartViewSet


router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')


urlpatterns = [
    path('carts/', CartViewSet.as_view({
        'get': 'list',
        # 'post': 'create'
    })),
    path('carts/<str:pk>', CartViewSet.as_view({
        'get': 'retrieve',
        # 'put': 'update',
        'delete': 'destroy'
    })),
]
urlpatterns += router.urls
