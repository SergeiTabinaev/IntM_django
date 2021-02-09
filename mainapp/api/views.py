from rest_framework import viewsets
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    ProductListRetrieveSerializer,
    CategoryDetailSerializer, CartProductSerializer, CartSerializer, CustomerSerializer)
from ..models import Category, Product, Cart, CartProduct, Customer

from rest_framework import viewsets, status
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    action_to_serializer = {
            'retrieve': CategoryDetailSerializer
        }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    action_to_serializer = {
        'list': ProductListRetrieveSerializer,
        'retrieve': ProductListRetrieveSerializer
    }

    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action,
            self.serializer_class
        )

class CartViewSet(viewsets.ViewSet):

    def list(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    # def create(self, request):
    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        cart_product = CartProduct.objects.get(id=pk)
        serializer = CartProductSerializer(cart_product)
        return Response(serializer.data)

    # def update(self, request, pk=None):
    #     product = Product.objects.get(id=pk)
    #     serializer = ProductSerializer(instance=product, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        cart_product = CartProduct.objects.get(id=pk)
        cart_product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
