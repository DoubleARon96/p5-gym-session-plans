from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse


def index(request):
    """
    view to show template
    """
    return render (request, "home/index.html")
