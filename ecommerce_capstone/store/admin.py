from django.contrib import admin
from .models import Order, Payment, Product, Review, User, Cart

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Cart)