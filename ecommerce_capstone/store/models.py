from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import Product
# from django.contrib.auth.models import Review
# from django.contrib.auth.models import Order
# from django.contrib.auth.models import Payment
from django.db.models.deletion import CASCADE



# Create your models here.
class User(models.Model): 
    user= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    phonenumber= models.CharField(max_length=20, blank = True)
    address= models.CharField(max_length=20, blank = True)
    zip_code= models.IntegerField()
    state = models.CharField(max_length=20, blank = True)
    country = models.CharField(max_length=20, blank = True)
    
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    description= models.CharField(max_length=200)
    category= models.CharField(max_length=20)

class Review(models.Model):
    User= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    Product= models.ForeignKey(Product, on_delete=CASCADE, blank= False)
    comment= models.CharField(max_length=200)

class Order(models.Model):
    User= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    Product= models.ForeignKey(Product, on_delete=CASCADE, blank= False)
    price= models.IntegerField()


class Payment(models.Model):
    User= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    address = models.CharField(max_length=50, blank=False)
    card_number = models.IntegerField()
    expiration_date = models.IntegerField()



