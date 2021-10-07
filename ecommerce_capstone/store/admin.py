from django.contrib import admin
from .models import Order, Product, Review, User

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)