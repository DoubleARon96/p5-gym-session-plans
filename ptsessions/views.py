from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import PtSessions,Price
from django.contrib import messages
from basket.models import Basket,BasketItem

def index(request):
    """
    view to show template
    """
    queryset = PtSessions.objects.all()
    price = Price.objects.all()
    content = queryset
    title = "PT Sessions For Purchase"
    viewbag = {"contents": content,
               "price" : price,
               "title": title}
        
    return render (request, "ptsessions/index.html",viewbag)

def ptsession_view (request, session_id):
    queryset = get_object_or_404(PtSessions, id = session_id)
    mysessions = PtSessions.objects.filter(id=session_id)
    title = queryset.session_name
    template = "ptsessions/pt-sessions.html"

    viewbag = {
        'title': title,
        'content': queryset,
        'sessions': mysessions
    }
    return render (request,template, viewbag)
    
