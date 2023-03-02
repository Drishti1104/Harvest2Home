from django.urls import path
from .views import *

urlpatterns = [
    path("", index_frontend, name="index-frontend"),
    path("login", login, name="login"),
    path("register", register, name="register"),
    path("shop-grid", shop_grid, name="shop-grid"),
    path("product", product, name="product"),
    path("vendors-grid", vendors_grid, name="vendors-grid"),
    path("vendor-details", vendor_details, name="vendor-details"),
]
