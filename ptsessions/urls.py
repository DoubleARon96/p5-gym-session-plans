from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="ptsessions"),
    path("<int:session_id>/", views.ptsession_view, name="ptsession_view")
]