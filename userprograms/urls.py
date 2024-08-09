from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="userprograms"),
    # test
    path('<int:id>/', views.mysessions, name='mysessions'),
    path('userprogramsupdate/<int:id>/', views.updateView, name='userprograms_update_url'),
    path('userprograms_delete_url/<int:id>/', views.mainDeleteView, name='mainprograms_delete_url'),
    #path('<int:id>/exercise_delete_url/<int:session_id>/', views.deleteView, name='exercise_delete_url'),
    path('<int:id>/exercise_delete_url/<int:session_id>/', views.deleteView, name='delete_exercise')
    

]