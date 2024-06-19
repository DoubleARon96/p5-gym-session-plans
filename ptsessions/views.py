from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    """
    view to show template
    """
    #queryset = HomeNews.objects.all()
    #content = queryset
    #viewbag = {"contents": content}
        
    return render (request, "ptsessions/index.html")
