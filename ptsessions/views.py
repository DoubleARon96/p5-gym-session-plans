from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import PtSessions

def index(request):
    """
    view to show template
    """
    queryset = PtSessions.objects.all()
    content = queryset
    title = "PT Sessions For Purchase"
    viewbag = {"contents": content,
               "client": PtSessions.objects.first().client,
               "title": title}
        
    return render (request, "ptsessions/index.html",viewbag)
