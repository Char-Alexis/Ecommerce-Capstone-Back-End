from rest_framework import serializers, status
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer
from .serializers import *
from ecommerce_capstone.store.serializers import UserSerializer
from .models import *
# from .serializer import UserSerializer
from django.contrib.auth.models import User
from django.http.response import Http404

# Create your views here.


# class UserList(APIView):

#     permission_classes = [AllowAny]

#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def user(request):
   
    print('User', f"{request.user.id} {request.user.email} {request.user.username} ")
   
    if request.method == 'POST':
        request.user
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status- status.HTTP_204_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    pass

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

    #get by id
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    #update
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShoppingCartList(APIView):
    pass


# STRIPE
# class Payment(APIView):
#     get(self, request)
#      try:
#         return Payment.objects.get(pk=pk)
#     except Payment.DoesNotExist:
#         raise Http404


class Orders(APIView):
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)