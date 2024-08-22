from django.shortcuts import render
from rest_framework import generics
from market.models import (Stocking, Customer, Supermarket, Purchase)
from market.serializers import (StockSerializer,
                                CustomerSerializer,
                                MarketSerializer,
                                PurchaseSerializer)

# Create your views here.
class StockController(generics.ListCreateAPIView):
    queryset = Stocking.objects.all()
    serializer_class = MarketSerializer

class SupermarketController(generics.ListCreateAPIView):
    queryset = Supermarket.objects.all()
    serializer_class = MarketSerializer

class CustomerController(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = MarketSerializer

class PurchasesController(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = MarketSerializer