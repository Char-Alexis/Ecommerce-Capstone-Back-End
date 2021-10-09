from django.urls import path, include
# from .views import *
from store import views


urlpatterns = [
    path('all/', views.get_all_users),
    path('login/', views.get_all_users),

    path('product/', views.ProductList),
    path('product/<int:pk>/', views.ProductDetail),
    
    path('review/', views.Review),
    path('review/<int:user_id>', views.Review),


    path('order/', views.Order),

    path('payment/', views.Payment),
    path('payment/<int:user_id>/', views.Payment),
    
    path('cart/', views.Cart),
    path('cart/<int:user_id>', views.Cart),
    path('cart/delete/<int:user_id>', views.Cart),


]