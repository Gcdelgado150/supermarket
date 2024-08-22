from django.urls import path
from . import views

urlpatterns = [
    path('stockController/', views.StockController.as_view(), name="Stock Controller"),
    path('supermarketController/', views.SupermarketController.as_view(), name="Supermarket Controller"),
    path('customerController/', views.CustomerController.as_view(), name="Customer Controller"),
    path('purchases/', views.PurchasesController.as_view(), name="Purchases"),
]
