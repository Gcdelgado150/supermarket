from django.shortcuts import render
from rest_framework import viewsets
from market.models import (Stocking, Customer, Supermarket, Purchase, Product, Category)
from market.serializers import (StockSerializer,
                                CustomerSerializer,
                                MarketSerializer,
                                PurchaseSerializer, 
                                ProductsSerializer, 
                                CategoriesSerializer)
from market.filters import (StockFilterClass,
                            SupermarketFilterClass,
                            CustomerFilterClass,
                            PurchaseFilterClass,
                            ProductFilterClass,
                            CategoryFilterClass)
from dj_rql.drf import RQLFilterBackend

# Create your views here.
class StockController(viewsets.ModelViewSet):
    queryset = Stocking.objects.all()
    serializer_class = StockSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = StockFilterClass

class SupermarketController(viewsets.ModelViewSet):
    queryset = Supermarket.objects.all()
    serializer_class = MarketSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = SupermarketFilterClass

class CustomerController(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = CustomerFilterClass

class PurchasesController(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = PurchaseFilterClass

class ProductsController(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = ProductFilterClass

class CategoriesController(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = CategoryFilterClass
