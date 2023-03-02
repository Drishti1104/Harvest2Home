from django.urls import path
from .views import *

urlpatterns = [
    path("", index_frontend, name="index-frontend"),
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
    path("register", register, name="register"),
    path("postregister", postregister, name="postregister"),
]
