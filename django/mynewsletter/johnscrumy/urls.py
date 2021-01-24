
from . import views
from django.urls import include, path

urlpatterns = [
     path('', views.get_grading_parameters) 
]

