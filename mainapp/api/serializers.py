from rest_framework import serializers

from ..models import Product, Category, Cart, CartProduct, Customer
from specs.models import ProductFeatures, CategoryFeature


class CategoryFeatureSerializer(serializers.ModelSerializer):

    feature_name = serializers.CharField(required=True)
    unit = serializers.CharField(read_only=True)

    class Meta:
        model = CategoryFeature
        fields = [
            'feature_name', 'unit'
        ]


class ProductFeatureSerializer(serializers.ModelSerializer):

    feature = CategoryFeatureSerializer()
    value = serializers.CharField(required=True)

    class Meta:
        model = ProductFeatures
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    @staticmethod
    def get_products(obj):
        return ProductSerializer(
        Product.objects.filter(category=obj), many=True).data


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductListRetrieveSerializer(serializers.ModelSerializer): #что отображалость полная инфа

    category = CategorySerializer()
    features = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    @staticmethod
    def get_features(obj):
        return ProductFeatureSerializer(
            ProductFeatures.objects.filter(product=obj), many=True).data


class CustomerSerializer(serializers.ModelSerializer):

    # order =

    class Meta:
        model = Customer
        fields = '__all__'


class CartProductSerializer(serializers.ModelSerializer):

    product = ProductSerializer()
    user = CustomerSerializer()
    # cart = CartSerializer()

    class Meta:
        model = CartProduct
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):

    owner = CustomerSerializer()
    products = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = '__all__'

    @staticmethod
    def get_products(obj):
        return CartProductSerializer(
            CartProduct.objects.filter(cart=obj), many=True).data
