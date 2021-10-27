from django.contrib import admin
from .models import Delivery, Order, Payment, Product, User, Cart, Review

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Cart)
admin.site.register(Delivery)

# admin.site.register(Comment)