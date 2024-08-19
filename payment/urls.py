from django.urls import path
from django.contrib import admin
from . import views
from .webhooks import webhook

urlpatterns = [
    path("", views.Checkout, name="payment"),
    path("payment_success/<order_number>",
         views.Checkout_success, name="payment_success"),
    path("cache_payment_data/",
         views.Cache_Payment_data, name="cache_payment_data"),
    path("wh/", webhook, name="web_hook")
]
