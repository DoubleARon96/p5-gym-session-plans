from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeContent.as_view, name="home"),
]