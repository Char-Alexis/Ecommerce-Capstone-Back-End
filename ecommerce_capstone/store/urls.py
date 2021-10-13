from django.urls import path, include
# from .views import *
from store import views


urlpatterns = [
    path('all/', views.get_all_users),
    path('login/', views.get_all_users),

    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    
    path('review/', views.ReviewList.as_view()),
    path('review/<int:review>', views.ReviewList.as_view()),


    # path('order/', views.Order.as_view()),

    path('payment/', views.Payment.as_view()),
    path('payment/<int:user_id>/', views.Payment.as_view()),
    
    path('cart/', views.CartList.as_view()),
    path('cart/<int:user_id>', views.CartDetail.as_view()),
    path('cart/delete/<int:user_id>', views.CartDetail.as_view()),


]