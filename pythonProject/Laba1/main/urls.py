from django.urls import path
from . import views


urlpatterns = [
path('', views.index),
path('profile', views.profile_view, name="profile"),
path('register', views.register_view.as_view(), name="register"),
]
