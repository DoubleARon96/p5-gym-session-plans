from django.urls import path

from . import views

urlpatterns = [
    path("ptsessions/", views.index, name="ptsessions"),
    #path("add_to_basket/<int:Ptsessions>", views.Add_to_basket, name="add_to_basket")
]