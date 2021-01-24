
from django.http import HttpResponse 
from django.shortcuts import render

# Create your views here.

def get_grading_parameters(request): 
    return HttpResponse("Welcome to Django") 
