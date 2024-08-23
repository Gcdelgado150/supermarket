from rest_framework import serializers
from market.models import *

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocking
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supermarket
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Product
        fields = '__all__'
