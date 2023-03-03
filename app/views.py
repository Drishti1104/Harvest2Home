from django.shortcuts import render,redirect
from django.contrib import messages,auth
import pyrebase

# Create your views here.
config={
	"apiKey": "AIzaSyDmCBzUXgbBiJZGI-aLBKdEynLrzQ4Xo6Y",
    "authDomain": "http://harvest2home-bfcd6.firebaseapp.com",
    "databaseURL": "https://harvest2home-bfcd6-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "harvest2home-bfcd6",
    "storageBucket": "http://harvest2home-bfcd6.appspot.com",
    "messagingSenderId": "9991712811",
    "appId": "1:9991712811:web:270b0cdd4d91dff4ae3a6e",
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def index_frontend(request):
    return render(request, "app/frontend/index-frontend.html")

def login(request):
    # harvesttohome = database.child('Data').child('Name').get().val()
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = auth.sign_in_with_email_and_password(email,password)
    except:
        messages.success(request, "User does not exist. Please register.")
        return redirect("register")
    
    return render(request, "app/frontend/page-login.html",{"e":email})

def register(request):
    return render(request, "app/frontend/page-register.html")

def postregister(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = authe.create_user_with_email_and_password(email,password)
    except:
        messages.success(request, "Unable to register.")
        return redirect("register")
    uid = user['localId']
    data={"name":name, "status":"1"}
    database.child("users").child(uid).child("details").set(data)
    return render(request, 'app/frontend/page-register.html')

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