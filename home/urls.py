from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('sv/', views.showView, name='show_url'),
    path('update/<int:id>', views.updateView, name= 'update_url'),
    path('del/<int:id>', views.deleteView, name= 'delete_url'),
]