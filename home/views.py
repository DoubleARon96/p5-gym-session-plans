from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import HomeNews

class HomeContent(generic.ListView):
    queryset = HomeNews.objects.all()
    template_name = "home/index.html"

    def index(request):
        """
        view to show template
        """
        queryset = HomeNews.objects.all()
        viewbag = {"contents": content,
                "title": title}
        
        return render (request, "home/index.html",viewbag)
