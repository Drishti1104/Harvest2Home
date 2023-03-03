from django.db import models
from datetime import datetime
# Create your models here.

class User(models.Model):
    FName = models.CharField(max_length=15, default="First")
    LName = models.CharField(max_length=20, default="Last")
    Phone = models.CharField(max_length=10, default="0123456789")
    Email = models.EmailField(max_length=50, unique=True, default="Email")
    Passwd = models.CharField(max_length=250, default="Passwd")

    is_user = models.CharField(max_length=20, default="User")

    def __str__(self):
        return self.Email

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)