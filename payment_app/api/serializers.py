from rest_framework import serializers
from payment_app.models import Basket , BasketItem
from store_app.models import category , brand , clothes_product , image
from django.conf import settings


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = brand
        fields = ['id' , 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['id' , 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    brand = BrandSerializer()

    class Meta:
        model = clothes_product
        fields = ['name','category','price','brand','count','sale_price']


class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = BasketItem
        fields = ['id' , 'count' , 'product']


class BasketSerializer(serializers.ModelSerializer):
    basket_items = BasketItemSerializer(many=True, source='items')

    class Meta:
        model = Basket
        fields = ['id', 'user', 'basket_items']
