from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('profile', views.profile_view, name="profile"),
    path('register', views.register_view.as_view(), name="register"),


    path("add/<str:product_name>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<str:product_name>/", views.remove_from_cart, name="remove_from_cart"),
    path('cart', views.cart_detail, name="cart_detail"),

    path('orders_detail', views.orders_detail, name="orders_detail"),
    path('orders', views.orders, name="orders"),
    path('add_new_item', views.add_new_item, name="add_new_item"),
]
