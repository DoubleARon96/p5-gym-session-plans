from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView
from .models import HomeNews

#class HomeContent(generic.ListView):
#    queryset = HomeNews.objects.all()
#    template_name = "home/index.html"

def index(request):
    """
    view to show template
    """
    queryset = HomeNews.objects.all()
    content = queryset
    viewbag = {"contents": content}
        
    return render (request, "home/index.html",viewbag)
