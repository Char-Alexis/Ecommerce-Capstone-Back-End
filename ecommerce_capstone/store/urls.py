from django.urls import path, include
# from ecommerce_capstone.store.views import ReviewDetail
# from .views import *
from store import views


urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view()),

    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    
    path('review/', views.ReviewList.as_view()),
    path('review/get/<int:review>', views.ReviewDetail.as_view()),
    path('review/post/<int:review>', views.ReviewDetail.as_view()),

    path('order/', views.OrderList.as_view()),

    path('payment/', views.Payment.as_view()),
    path('payment/<int:user_id>/', views.Payment.as_view()),
    
    path('cart/', views.CartList.as_view()),
    path('cart/<int:user_id>', views.CartDetail.as_view()),
    path('cart/delete/<int:user_id>', views.CartDetail.as_view()),


]