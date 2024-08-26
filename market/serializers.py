from rest_framework import serializers
import re
from django.db import transaction
from market.models import *
import logging

logger = logging.getLogger('yourapp')

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
            superm = Supermarket.objects.get(name=value)
        except Category.DoesNotExist:
            raise serializers.ValidationError("Category with this name does not exist.")
        return superm

    def create(self, validated_data):
        product = validated_data.get('product')
        supermarket = validated_data.get('supermarket')
        amount = validated_data.get('amount')
        
        # Check if a Stocking instance with the same product and supermarket already exists
        stocking, created = Stocking.objects.get_or_create(
            product=product,
            supermarket=supermarket,
            defaults={'amount': amount}
        )
        
        if not created:
            # If it already existed, update the amount
            stocking.amount += amount
            stocking.save()

        return stocking
    
    def update(self, instance, validated_data):
        instance.supermarket = validated_data.get('supermarket', instance.supermarket)
        instance.product = validated_data.get('product', instance.product)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance

class CustomerSerializer(serializers.ModelSerializer):
    def validate_cpf(self, value):
        value = re.sub(r'\D', '', value)  # Remove non-digit characters
        if len(value) != 11 or value.isdigit() == False:
            raise serializers.ValidationError("cpf invalid")
        return value

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.subscription_type = validated_data.get('subscription_type', instance.subscription_type)
        instance.save()
        return instance
    
    class Meta:
        model = Customer
        fields = '__all__'

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supermarket
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    customer = serializers.CharField()
    supermarket = serializers.CharField()
    product = serializers.CharField()

    def validate_customer(self, value):
        try:
            customer = Customer.objects.get(name=value)
        except Customer.DoesNotExist:
            raise serializers.ValidationError("Customer does not exist.")
        return customer

    def validate_supermarket(self, value):
        """Supermarket is not registered."""
        try:
            supermarket = Supermarket.objects.get(name=value)
        except Supermarket.DoesNotExist:
            raise serializers.ValidationError("Supermarket with this name does not exist.")
        return supermarket
    
    def validate_product(self, value):
        """Supermarket is not registered."""
        try:
            product = Product.objects.get(name=value)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product with this name does not exist.")
        return product

    def validate(self, data):
        product = data.get('product')
        supermarket = data.get('supermarket')
        amount = data.get('amount')

        # Check if the product is in stock
        try:
            stock = Stocking.objects.get(product=product, supermarket=supermarket)
        except Stocking.DoesNotExist:
            raise serializers.ValidationError("Product does not exist in this supermarket.")

        # Check if the requested quantity exceeds available stock
        if amount > stock.amount:
            raise serializers.ValidationError(f"Requested amount exceeds available stock for product '{product}'")

        return data

    def create(self, validated_data):
        product = validated_data['product']
        supermarket = validated_data['supermarket']
        amount = validated_data['amount']

        # Deduct stock for the purchased product
        try:
            stock = Stocking.objects.get(product=product, supermarket=supermarket)
            if amount > stock.amount:
                raise serializers.ValidationError(f"Requested amount exceeds available stock for product '{product.name}'")
            stock.amount -= amount
            stock.save()
        except Stocking.DoesNotExist:
            raise serializers.ValidationError("Product does not exist in this supermarket.")

        return Purchase.objects.create(**validated_data)

    def update(self, instance, validated_data):
        product = validated_data.get('product', instance.product)
        supermarket = validated_data.get('supermarket', instance.supermarket)
        amount = validated_data.get('amount', instance.amount)

        # Deduct stock for the purchased product
        try:
            stock = Stocking.objects.get(product=product, supermarket=supermarket)
            if amount > stock.amount:
                raise serializers.ValidationError(f"Requested amount exceeds available stock for product '{product.name}'")
            stock.amount -= amount
            stock.save()
        except Stocking.DoesNotExist:
            raise serializers.ValidationError("Product does not exist in this supermarket.")

        # Restore previous stock amount before updating
        previous_amount = instance.amount
        if instance.product == product and instance.supermarket == supermarket:
            stock.amount += previous_amount

        instance.customer = validated_data.get('customer', instance.customer)
        instance.supermarket = supermarket
        instance.product = product
        instance.amount = amount
        instance.date = validated_data.get('date', instance.date)
        instance.payment_method = validated_data.get('payment_method', instance.payment_method)
        instance.save()

        return instance

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