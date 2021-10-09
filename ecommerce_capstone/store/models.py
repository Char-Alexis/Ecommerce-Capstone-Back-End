from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import Product
# from django.contrib.auth.models import Review
# from django.contrib.auth.models import Order
# from django.contrib.auth.models import Payment
from django.db.models.deletion import CASCADE



# Create your models here.
class User(models.Model): 
    user_id= models.ForeignKey(User, on_delete=CASCADE, blank= False)
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
    price = models.FloatField()
    description= models.CharField(max_length=200)
    category= models.CharField(max_length=20)
    image = models.ImageField(upload_to='upload/', blank= True, null= True)
    
    def get_image(self):
        if self.image:
            return 'http://127/0/01:8000' + self.image.url
        return ''

class Review(models.Model):
    user_id= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    product_id= models.ForeignKey(Product, on_delete=CASCADE, blank= False)
    comment= models.CharField(max_length=200)

class Payment(models.Model):
    user_id= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    address = models.CharField(max_length=50, blank=False)
    card_number = models.IntegerField()
    expiration_date = models.CharField(max_length=5, help_text='00/00', blank= False)
    
class Order(models.Model):
    user_id= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    product_id= models.ForeignKey(Product, on_delete=CASCADE, blank= False)
    price= models.FloatField()


class Cart(models.Model):
    user_id= models.ForeignKey(User, on_delete=CASCADE, blank= False)
    product_id= models.ForeignKey(Product, on_delete=CASCADE, blank= False)



