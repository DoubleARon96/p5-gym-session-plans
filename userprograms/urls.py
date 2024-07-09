from django.urls import path

from . import views

urlpatterns = [
    path("userprograms/", views.index, name="userprograms"),
    # test
    path('userprograms/<int:id>/', views.mysessions, name='mysessions'),
    path('update/<int:ids>/', views.updateView, name= 'update_url'),
]