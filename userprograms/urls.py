from django.urls import path

from . import views

urlpatterns = [
    path("userprograms/", views.index, name="userprograms")
]