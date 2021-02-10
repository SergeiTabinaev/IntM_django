from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.status import HTTP_400_BAD_REQUEST

from .serializers import (
    ProductSerializer,
    CategorySerializer,
    ProductListRetrieveSerializer,
    CategoryDetailSerializer, CartProductSerializer, CartSerializer, CustomerSerializer)
from ..mixins import CartMixin
from ..models import Category, Product, Cart, CartProduct, Customer

from rest_framework import viewsets, status
from rest_framework.response import Response

from ..utils import recalc_cart


class CategoryViewSet(CartMixin, viewsets.ModelViewSet): #,

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


class ProductViewSet(CartMixin, viewsets.ModelViewSet): #

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


class CartViewSet(CartMixin, viewsets.ViewSet): #

    def list(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        cart = Cart.objects.get(id=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        cart_product = CartProduct.objects.get(id=pk)
        cart_product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartProductViewSet(CartMixin, viewsets.ViewSet): #,

    def list(self, request):
        cartProducts = CartProduct.objects.all()
        serializer = CartProductSerializer(cartProducts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        cartProduct = CartProduct.objects.get(id=pk)
        serializer = CartProductSerializer(cartProduct)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        cart_product = CartProduct.objects.get(id=pk)
        cart_product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # class ChangeQTYView(CartMixin, View):
    #
    #     def post(self, request, *args, **kwargs):
    #         product_slug = kwargs.get('slug')
    #         product = Product.objects.get(slug=product_slug)
    #         cart_product = CartProduct.objects.get(
    #             user=self.cart.owner, cart=self.cart, product=product
    #         )
    #         qty = int(request.POST.get('qty'))
    #         cart_product.qty = qty
    #         cart_product.save()
    #         recalc_cart(self.cart)
    #         messages.add_message(request, messages.INFO, "Кол-во успешно изменено")
    #         return HttpResponseRedirect('/cart/')


class AddToCartViewSet(CartMixin, viewsets.ViewSet):

    def retrieve(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        product = Product.objects.get(slug=product_slug)
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner, cart=self.cart, product=product
        )
        if created:
            self.cart.products.add(cart_product)
        recalc_cart(self.cart)
        return Response(status=status.HTTP_201_CREATED)
