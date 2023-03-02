from django.urls import path
from .views import *

urlpatterns = [
    path("", index_frontend, name="index-frontend"),
    path("login", login, name="login"),
    path("register", register, name="register"),
]
