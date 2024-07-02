from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import PtSessions,Price

def index(request):
    """
    view to show template
    """
    queryset = PtSessions.objects.all()
    price = Price.objects.all()
    content = queryset
    viewbag = {"contents": content,
               "price": price,
               "client": PtSessions.client}
        
    return render (request, "ptsessions/index.html",viewbag)
