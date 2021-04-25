from rest_framework import serializers
from shop.models import Product, Cart,  CartItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"


class CartItemListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='product.name')

    class Meta:
        model = CartItem
        fields = ['id', 'name', 'amount']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemListSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = "__all__"