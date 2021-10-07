from django.urls import path
# from .views import *
from store import views

urlpatterns = [
    path('all/', views.get_all_users),
    path('login/', views.get_all_users),

    path('product/', views.ProductList),
    path('product/<int:pk>/', views.ProductDetail),
    
    path('review/', views.Review),

    path('order/', views.Order),

    path('payment/', views.Payment),
    path('payment/<int:User_id>/', views.Payment),
    
    path('cart/', views.get_all_users),
    path('cart/<int:User_id>', views.get_all_users),
    path('cart/delete/<int:User_id>', views.get_all_users),


]