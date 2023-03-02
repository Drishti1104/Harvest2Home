from django.shortcuts import render
import pyrebase

# Create your views here.

def index_frontend(request):
    return render(request, "app/frontend/index-frontend.html")

def login(request):
    return render(request, "app/frontend/page-login.html")

def register(request):
    return render(request, "app/frontend/page-register.html")