from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib import admin
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView
from .forms import NewsForm
from .models import HomeNews


def index(request):
    """
    view to show template
    """
    queryset = HomeNews.objects.all()
    content = queryset
    title = "Welcome To Valkan Fitness"
    viewbag = {"contents": content,
               "title": title}

    return render(request, "home/index.html", viewbag)


def NewsFormView(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST)
        title = "News Forms"
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'home/crud.html'
    context = {'form': form,
               "title": title}
    return render(request, template_name, context)


def showView(request):
    storyShow = HomeNews.objects.all()
    template_name = 'home/show.html'
    context = {'show': storyShow}
    return render(request, template_name, context)


def updateView(request, ids):
    queryset = get_object_or_404(HomeNews, id=ids)
    form = NewsForm(instance=queryset)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, "Message Was Updated Successfully !")
            return redirect('home')
        else:
            form = NewsForm(instance=queryset)
            messages.error(request, "Message Was Not Updated !")
    template_name = 'home/crud.html'
    return render(request, template_name, {'form': form})
