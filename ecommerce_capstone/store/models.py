from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import Product
# from django.contrib.auth.models import Review
# from django.contrib.auth.models import Order
# from django.contrib.auth.models import Payment
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import *




# Create your models here.
class User(models.Model): 
    user_id= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    phone_number= models.CharField(max_length=20, default=0, blank = True)
    address= models.CharField(max_length=20, blank = True)
    zip_code= models.IntegerField()
    state = models.CharField(max_length=20, blank = True)
    country = models.CharField(max_length=20, blank = True)

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.FloatField()
    description= models.CharField(max_length=200)
    category= models.CharField(max_length=20)
    

class Review(models.Model):
    user_id= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    product_id= models.ForeignKey(Product, on_delete=CASCADE, blank= False)
    comment= models.CharField(max_length=200)

class Payment(models.Model):
    user_id= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    # cart_id = models.ForeignKey(Cart, null=True, on_delete=CASCADE)
    card_number = models.IntegerField()
    expiration_date = models.CharField(max_length=5, help_text='00/00', blank= False)
    total = models.DecimalField(default=0, max_digits=6, decimal_places=2)

class Order(models.Model):
    user_id= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    product_id= models.ForeignKey(Product, on_delete=CASCADE, blank= False)
    price= models.FloatField(default=0)


class Cart(models.Model):
    user_id= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    product_id= models.ForeignKey(Product, on_delete=CASCADE, blank= False)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)

class Delivery(models.Model):
    user_id= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    product_id= models.ForeignKey(Product, on_delete=CASCADE, blank= False)
    # address=
    # state=
    # zip_code=
    # country=




