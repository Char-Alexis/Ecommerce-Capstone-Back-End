from rest_framework import serializers, status
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from .serializers import *
# from ecommerce_capstone.store.serializers import UserSerializer
from .models import *
# from .serializer import UserSerializer
from django.contrib.auth.models import User
from store import models
from django.http.response import Http404
import json
from django.http import JsonResponse
# from django.http.response import JsonResponse

# import stripe
# stripe.api_key = 'sk_test_51JiRtyCwgXG48Eq1Su24DN4inPyT8E6jOfLdsHTfkU3gKLyU9g7sg3r0npAzSxPXSwjdb893TVvT3BhCkO1lAc0800YZxMSY2F'
# Create your views here.

# @api_view(['GET'])
# @permission_classes([AllowAny])

class UserList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# @api_view(['POST', 'GET'])
# @permission_classes([AllowAny])
# def user(request):
   
#     print('User', f"{request.user.id} {request.user.email} {request.user.username} ")
   
#     if request.method == 'POST':
#         request.user
        
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             return Response(serializer.data, status- status.HTTP_204_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self, user):
        try:
                return User.objects.get(id=user)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, user):
        user = self.get_object(id=user)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def put(self, request, user):
            user = self.get_object(user)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post (self, request):
    #     users = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # pass
      

class ProductList(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    
    def get_object(self, pk):
            try:
                return Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class CommentDetail(APIView):
#     def get_object(self, comment):
#             try:
#                 return Comment.objects.filter(id=comment)
#             except Comment.DoesNotExist:
#                 raise Http404

#     def get(self, request, comment):
#         try:
#             comment = self.get_object(comment)
#             serializer = CommentSerializer(comment, many=True)
#             return Response(serializer.data)
#         except Comment.DoesNotExist:
#             raise Http404


#     def put(self, request, pk):
#         comment = self.get_object(pk)
#         serializer = CommentSerializer(comment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def post(self, request, comment):
#         serializer = CommentSerializer(comment,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
#     def delete(self, request, pk):
#         comment = self.get_object(pk)
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CommentUser(APIView):
#     def get_object(self, user):
#         try:
#             return Comment.objects.filter(user=user)
#         except Comment.DoesNotExist:
#             raise Http404
#     def get(self, request, user):
#             try:
#                 comment = self.get_object(user)
#                 serializer = CommentSerializer(comment)
#                 return Response(serializer.data)
#             except Comment.DoesNotExist:
#                 raise Http404
#     def post(self, request):
#             print(request.data)

#             serializer = CommentSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewList(APIView):

    def get(self, request):
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetail(APIView):
    def get_object(self, review):
            try:
                return Review.objects.filter(id=review)
            except Review.DoesNotExist:
                raise Http404

    def get(self, request, review):
        try:
            review = self.get_object(review)
            serializer = ReviewSerializer(review, many=True)
            return Response(serializer.data)
        except Review.DoesNotExist:
            raise Http404


    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, review):
        serializer = ReviewSerializer(review,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewUser(APIView):
    def get_object(self, user):
                try:
                    return Review.objects.filter(user=user)
                except Review.DoesNotExist:
                    raise Http404
    def get(self, request, user):
            try:
                review = self.get_object(user)
                serializer = ReviewSerializer(review)
                return Response(serializer.data)
            except Review.DoesNotExist:
                raise Http404
    def post(self, request):
            print(request.data)

            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeliveryList(APIView):
    def get(self, request, delivery):
        delivery = Order.objects.all()
        serializer = DeliverySerializer(delivery, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeliverySerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

# class Payment(APIView):
#     def get(self, request):
#         payment = Payment.objects.all()
#         serializer = PaymentSerializer(payment, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PaymentSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)


class CartList(APIView):
    def get(self, request):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

    def post(self, request):
        body=json.loads(request.body)
        product_id, quantity = body["product_id"], body["quantity"]
        user_id = models.User.objects.get(username = body["username"])
        data=dict(
            product_id = Product.objects.get(id = product_id),
            quantity=quantity,
            user_id = user_id,
        )
        instance = Cart.objects.create(**data)


        return JsonResponse(dict(product_id=instance.product_id.id, user_id=instance.user_id.id),status=status.HTTP_201_CREATED, safe=False)
    
class CartDetail(APIView):

    def get_object(self, user):
        try:
            return Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            raise Http404

    def get(self, request, user):
        try:
            cart = self.get_object(user)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            raise Http404

    def put(self, request, user):
        cart = self.get_object(user)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user):
        cart = self.get_object(user)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        

class StripeKey(APIView):
    def get(self, request):
        key={'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(key, safe=False)