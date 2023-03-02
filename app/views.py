from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages,auth
import pyrebase

config={
	"apiKey": "AIzaSyDDLYuixXMJTNOMk-2RRMaEhzkyB5lLR2c",
    "authDomain": "http://harvesttohome-f0370.firebaseapp.com",
    "databaseURL": "https://harvesttohome-f0370-default-rtdb.firebaseio.com",
    "projectId": "harvesttohome-f0370",
    "storageBucket": "http://harvesttohome-f0370.appspot.com",
    "messagingSenderId": "370734253592",
    "appId": "1:370734253592:web:3b8aca62f7cf97d38ae56d",
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

# def home(request):
# 	day = database.child('Data').child('Day').get().val()
# 	id = database.child('Data').child('Id').get().val()
# 	projectname = database.child('Data').child('Projectname').get().val()
# 	return render(request,"Home.html",{"day":day,"id":id,"projectname":projectname })

# Create your views here.

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
    
    return render(request, "app/frontend/index-frontend.html")

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