from django.urls import path
from .views import *

urlpatterns = [
    path("", index_frontend, name="index-frontend"),
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
    path("register", register, name="register"),
    path("postregister", postregister, name="postregister"),
    path("shop-grid", shop_grid, name="shop-grid"),
    path("product", product, name="product"),
    path("vendors-grid", vendors_grid, name="vendors-grid"),
    path("vendor-details", vendor_details, name="vendor-details"),
    path("cart", cart, name="cart"),
    path("checkout", checkout, name="checkout"),
    path("wishlist", wishlist, name="wishlist"),
]
