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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout

class LoginView(APIView):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # This will set the session cookie
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

from django.http import JsonResponse
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.http import HttpResponse

def set_custom_cookie(request):
    response = HttpResponse("Setting a custom cookie")
    
    # Set a cookie with a 30-day expiration
    expires = datetime.utcnow() + timedelta(days=30)
    response.set_cookie('custom_cookie', 'value', expires=expires, httponly=True, secure=True)
    
    return response

def get_user_info(request):
    sessionid = request.COOKIES.get('sessionid')
    if not sessionid:
        return JsonResponse({'error': 'No session ID provided'}, status=400)

    try:
        session = Session.objects.get(pk=sessionid)
        user_id = session.get_decoded().get('_auth_user_id')
        user = get_user_model().objects.get(pk=user_id)
        return JsonResponse({'username': user.username})
    except Session.DoesNotExist:
        return JsonResponse({'error': 'Invalid session ID'}, status=400)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=400)