from dj_rql.filter_cls import AutoRQLFilterClass, FilterLookups
from market.models import *

class SupermarketFilterClass(AutoRQLFilterClass):
    MODEL = Supermarket
    
class CustomerFilterClass(AutoRQLFilterClass):
    MODEL = Customer

class CategoryFilterClass(AutoRQLFilterClass):
    MODEL = Category

class ProductFilterClass(AutoRQLFilterClass):
    MODEL = Product
    FILTERS = [
        {
            'filter': 'category',
            'source': 'category__name'
        },
    ]

class StockFilterClass(AutoRQLFilterClass):
    MODEL = Stocking
    FILTERS = [
        {
            'filter': 'supermarket',
            'source': 'supermarket__name'
        },
        {
            'filter': 'product',
            'source': 'product__name'
        },
    ]
    

class PurchaseFilterClass(AutoRQLFilterClass):
    MODEL = Purchase
    FILTERS = [
        {
            'filter': 'customer',
            'source': 'customer__name'
        },
        {
            'filter': 'supermarket',
            'source': 'supermarket__name'
        },
        {
            'filter': 'product',
            'source': 'product__name'
        },
    ]
