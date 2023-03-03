from django.shortcuts import render,redirect
from django.contrib import messages,auth
import pyrebase

# Create your views here.

def index_frontend(request):
    return render(request, "app/frontend/index-frontend.html")

# def login(request):
#     # harvesttohome = database.child('Data').child('Name').get().val()
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     try:
#         user = authe.sign_in_with_email_and_password(email,password)
#         return redirect("index-page")
        
#     except:
#         messages.success(request, "User does not exist. Please register.")
#         return redirect("register")
    
def login_page(request):
    return render(request, "app/frontend/page-login.html")

def register(request):
    return render(request, "app/frontend/page-register.html")

def logout(request):
    auth.logout(request)
    return render(request, 'app/frontend/index-frontend.html')

def shop_grid(request):
    return render(request, "app/frontend/shop-grid-left.html")

def product(request):
    return render(request, "app/frontend/shop-product-full.html")

def vendors_grid(request):
    return render(request, "app/frontend/vendors-grid.html")

def vendor_details(request):
    return render(request, "app/frontend/vendor-details.html")

def cart(request):
    return render(request, "app/frontend/shop-cart.html")

def checkout(request):
    return render(request, "app/frontend/shop-checkout.html")

def wishlist(request):
    return render(request, "app/frontend/shop-wishlist.html")