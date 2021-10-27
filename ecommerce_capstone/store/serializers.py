from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','username', 'password']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'price', 'description', 'category']

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ['id', 'user_id', 'product_id', 'comment']


# class CommentSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Comment
#         fields = ['id', 'username', 'product_id', 'comment']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'card_number', 'expiration_date', 'total']

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['id', 'price']
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['id', 'product_id','notes']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user_id', 'product_id', 'quantity']
