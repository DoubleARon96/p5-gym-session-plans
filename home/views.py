from django.shortcuts import render, redirect
from django.contrib import admin
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView
from .forms import NewsForm
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

def NewsFormView(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'home/crud.html'
    context = {'form': form}
    return render(request, template_name, context)

def showView(request):
    storyShow = HomeNews.objects.all()
    template_name = 'home/show.html'
    context = {'show': storyShow}
    return render(request, template_name, context)

def deleteView(request, f_oid):
    queryset = HomeNews.objects.get(oid=f_oid)
    if request.method == 'POST':
        queryset.delete()
        return redirect('show_url')
    template_name = 'home/confirmation.html'
    context = {'deleteview': queryset}
    return render(request, template_name, context)

def updateView(request, f_oid):
    queryset = HomeNews.objects.get(id = f_oid)
    form = NewsForm(instance=queryset)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'home/list_homenews.html'
    context = {'updateview': form}
    return render(request, template_name, context)
