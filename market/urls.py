from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('stockController', views.StockController)
router.register('supermarketController', views.SupermarketController)
router.register('customerController', views.CustomerController)
router.register('purchases', views.PurchasesController)
router.register('productsController', views.ProductsController)
router.register('categoriesController', views.CategoriesController)

urlpatterns = [
    path('', include(router.urls)),
]
