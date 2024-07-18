from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import PtSessions,Price
#from basket.models import 

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

def Add_to_basket (request, Ptsessions):
    item = get_object_or_404(PtSessions, id=id)
    #basket = 
