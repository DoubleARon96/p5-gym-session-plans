from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
path("", views.basket_view, name="basket"),
path("adjust_basket/<int:session_id>", views.adjust_basket, name="adjust_basket"),
path("add_to_basket/<int:session_id>", views.add_to_basket, name="add_to_basket")
]