from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('sv/', views.showView, name='show_url'),
    path('update/<int:ids>/', views.updateView, name= 'update_url'),
]