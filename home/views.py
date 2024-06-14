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

def NewsFormView(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'crudapp/order.html'
    context = {'form': form}
    return render(request, template_name, context)
