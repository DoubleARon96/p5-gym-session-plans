from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import admin
from django.http import HttpResponse
from django.views import generic
from .models import Profile

# Create your views here.
def index(request):
    """
    view to show template
    """
    #queryset = get_object_or_404(Profile)
    queryset = Profile.objects.all()
    content = queryset
    viewbag = {"contents": content}
        
    return render (request, "profile_page/index.html",viewbag)