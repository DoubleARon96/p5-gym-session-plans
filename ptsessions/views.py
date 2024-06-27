from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import PtSessions

def index(request):
    """
    view to show template
    """
    queryset = PtSessions.objects.all()
    content = queryset
    viewbag = {"contents": content}
        
    return render (request, "ptsessions/index.html",viewbag)
