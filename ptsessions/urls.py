from django.urls import path
from django.contrib import admin


from . import views

urlpatterns = [
    path("", views.index, name="ptsessions"),
    path("<int:session_id>/", views.ptsession_view, name="ptsession_view"),
    path('admin/', admin.site.urls),
]