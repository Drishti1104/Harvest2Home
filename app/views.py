from django.shortcuts import render
import pyrebase

# Create your views here.

def index_frontend(request):
    return render(request, "app/frontend/index-frontend.html")

def login(request):
    return render(request, "app/frontend/page-login.html")

def register(request):
    return render(request, "app/frontend/page-register.html")

def shop_grid(request):
    return render(request, "app/frontend/shop-grid-left.html")

def product(request):
    return render(request, "app/frontend/shop-product-full.html")

def vendors_grid(request):
    return render(request, "app/frontend/vendors-grid.html")

def vendor_details(request):
    return render(request, "app/frontend/vendor-details.html")