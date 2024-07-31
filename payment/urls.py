from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
path("", views.Checkout, name="payment"),
path("payment_success/<order_number>", views.Checkout_success, name="payment_success")
]