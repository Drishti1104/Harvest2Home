from django.db import models
from datetime import datetime
# Create your models here.

class User(models.Model):
    Name = models.CharField(max_length=15, default="Name")
    Email = models.EmailField(max_length=50, unique=True, default="Email")
    Phone = models.CharField(max_length=10, default="0123456789")
    Address = models.TextField(max_length=200, default="abc xyz ")
    Pin_code = models.IntegerField(max_length=10, default="000000")
    Passwd = models.CharField(max_length=250, default="Passwd")
    is_user = models.CharField(max_length=20, default="User")

    def __str__(self):
        return self.Email