from django.urls import path
from . import views

urlpatterns = [
    path("userprograms/", views.index, name="userprograms"),
    # test
    path('userprograms/<int:id>/', views.mysessions, name='mysessions'),
    path('userprogramsupdate/<int:id>/', views.updateView, name='userprograms_update_url'),
    path('userprogramsdelete/<int:exercise_id>/', views.deleteView, name='userprograms_delete_url')
]