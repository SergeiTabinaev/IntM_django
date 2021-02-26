from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import (
    ProductSerializer,
    CategorySerializer,
    ProductListRetrieveSerializer,
    CategoryDetailSerializer,
    CartProductSerializer,
    CartSerializer,
    CustomerSerializer)

from ..models import Category, Product, Cart, CartProduct, Customer

from ..mixins import CartMixin   # Логика определения пользователя корзины, либо присваивания пользователю значения - анонимный пользователь
from ..utils import recalc_cart  # Расчет значений общей суммы товаров в корзине


class CategoryViewSet(CartMixin, viewsets.ModelViewSet):
    """ вывод списка товаров в категории """

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


class ProductViewSet(CartMixin, viewsets.ModelViewSet):
    """ вывод списка товаров и конкретного товара """

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


class CartViewSet(CartMixin, viewsets.ViewSet):
    """ вывод список корзин, конкретной корзины """

    def list(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        cart = Cart.objects.get(id=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class CartProductViewSet(CartMixin, viewsets.ViewSet):
    """ вывод списка товаров корзины пользователя, удаление товара """

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


class AddToCartViewSet(CartMixin, APIView):
    """ добавление товара в корзину """

    def post(self, request, *args, **kwargs):
        product_slug = kwargs.get('slug')
        product = Product.objects.get(slug=product_slug)
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner or request.user, cart=self.cart, product=product
        )
        if created:
            self.cart.products.add(cart_product)
        recalc_cart(self.cart)  # Расчет значений общей суммы товаров в корзине
        return Response(status=status.HTTP_201_CREATED)


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
