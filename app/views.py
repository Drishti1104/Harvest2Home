from django.shortcuts import render, redirect
import imp
from django.contrib import messages
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.conf import settings
import random
from django.http import JsonResponse
from django.db.models import Count
from dateutil.relativedelta import relativedelta
from datetime import datetime
from dateutil import tz
# Create your views here.

def index_frontend(request):
    return render(request, "app/frontend/index-frontend.html")
    
def login_page(request):
    if request.method == "POST":
        email = request.POST['Email'].lower()
        pswd = request.POST['Password']
        fnd = User.objects.filter(Email = email)
        if len(fnd) > 0:
            if check_password(pswd, fnd[0].Passwd):
                # if pswd == fnd[0].Passwd:
                request.session['id'] = fnd[0].id
                request.session['email'] = fnd[0].Email
                request.session['is_user'] = fnd[0].is_user
                
                return redirect("dashboard")
            else:
                messages.error(request, "Please enter a valid password")
                return redirect("login")
        else:
            messages.error(request, "User does not exist. Please register.")
            return redirect("register")
    else:
        return render(request, "app/login.html")

def send_otp_email(otp, email):
    subject = "Verify your Email - {}".format(email)
    print(otp)
    message = "Your 4-digit OTP to verify your account is : " + str(otp) + ". Please don't share it with anyone else"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def send_psw_email(otp, email):
    subject = "Reset your Password - {}".format(email)
    print(otp)
    message = "Your 4-digit OTP to reset your password is : " + str(otp) + ". Please don't share it with anyone else"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def send_otp_email(otp, email):
    subject = "Verify your Email - {}".format(email)
    print(otp)
    message = "Your 4-digit OTP to verify your account is : " + str(otp) + ". Please don't share it with anyone else"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def send_psw_email(otp, email):
    subject = "Reset your Password - {}".format(email)
    print(otp)
    message = "Your 4-digit OTP to reset your password is : " + str(otp) + ". Please don't share it with anyone else"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def register(request):
    if request.method == "POST":
        fnd = User.objects.filter(Email = request.POST['email'].lower())
        if len(fnd) == 0:
            request.session['username'] = request.POST['username']
            request.session['email'] = request.POST['email'].lower()
            request.session['number'] = request.POST['number']
            request.session['address'] = request.POST['address']
            request.session['pincode'] = request.POST['pincode']
            request.session['password'] = request.POST['password']
            cpswd = request.POST['confirm-password']

            # Register Without OTP Verification
            name = request.POST['username']
            email = request.POST['email'].lower()
            number = request.POST['number']
            address = request.POST['address']
            pincode = request.POST['pincode']
            pswd = request.POST['password']
            cpswd = request.POST['confirm-password']
            if request.session['pswd'] == cpswd:
                request.session['pswd'] = make_password(request.POST['password'])
                request.session['otp'] = random.randint(1000,9999)
                send_otp_email(request.session['otp'], request.session['email'])
                messages.success(request, "OTP is sent to your email. Please enter it.")
                return redirect("verifyotppage")
                
                # Register Without OTP Verification
            if pswd == cpswd:
                AddUser = User.objects.create(
                    Name = name,
                    Email = email,
                    Phone = number,
                    Address = address,
                    Pin_code = pincode,
                    Passwd = pswd
                )
                messages.success(request, "You have registered successfully. Please login to continue")
                return redirect("login")
            else:
                messages.error(request, "Password and Confirm Password do not match. Please try again")
                return redirect("register")
        else:
            messages.error(request, "User already exists. Please login")
            return redirect("login")
    else:
        return render(request, "app/frontend/page-register.html")


def logout(request):
    return render(request, 'app/frontend/index-frontend.html')
# def logout(request):
    #  if 'email' in request.session:
    #     del request.session['id']
    #     del request.session['email']
    #     del request.session['is_user']
    #     return redirect("login")
    # else:
    #     return redirect("login")
    # return render(request, 'app/frontend/index-frontend.html')

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

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
]
