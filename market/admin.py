from market.models import (Customer, 
                           Supermarket, 
                           Category, 
                           Product, 
                           Stocking, 
                           Purchase)
from django.contrib import admin

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'subscription_type', )
    search_fields = ('name', 'subscription_type', )
    list_filter = ('subscription_type', )
    
class SupermarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', )
    search_fields = ('name', 'city', )
    list_filter = ('city', )
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_filter = ('name', )
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', )
    search_fields = ('name', )
    list_filter = ('name', 'category', )
    
class StockingAdmin(admin.ModelAdmin):
    list_display = ('supermarket', 'product', )
    search_fields = ('supermarket', 'product', )
    list_filter = ('supermarket', 'product', )

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'supermarket', 'product', 'date', 'payment_method', )
    search_fields = ('customer', 'supermarket', 'product', 'date', 'payment_method', )
    list_filter = ('customer', 'supermarket', 'product', 'date', 'payment_method', )
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Supermarket, SupermarketAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Stocking, StockingAdmin)
admin.site.register(Purchase, PurchaseAdmin)
