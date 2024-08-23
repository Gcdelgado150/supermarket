from rest_framework import serializers
from market.models import *

class StockSerializer(serializers.ModelSerializer):
    supermarket = serializers.CharField()
    product = serializers.CharField()

    class Meta:
        model = Stocking
        fields = '__all__'

    def validate_amount(self, value):
        """Ensure that the amount is a positive integer."""
        if value <= 0:
            raise serializers.ValidationError("Amount must be a positive integer.")
        return value
    
    def validate_product(self, value):
        """Product is not registered."""
        try:
            category = Product.objects.get(name=value)
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category with this name does not exist.")
        return category
    
    def validate_supermarket(self, value):
        """Supermarket is not registered."""
        try:
            category = Supermarket.objects.get(name=value)
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category with this name does not exist.")
        return category

    def create(self, validated_data):
        return Stocking.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.supermarket = validated_data.get('supermarket', instance.supermarket)
        instance.product = validated_data.get('product', instance.product)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance


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
    category = serializers.CharField()

    class Meta:
        model = Product
        fields = '__all__'

    def validate_category(self, value):
        try:
            category = Category.objects.get(name=value)
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category with this name does not exist.")
        return category

    def create(self, validated_data):
        category = validated_data.pop('category')
        return Product.objects.create(category=category, **validated_data)