from django.urls import path

from . import views

urlpatterns = [
    path("ptsessions/", views.index, name="ptsessions"),
]