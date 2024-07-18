from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import BasketItem, Basket
from ptsessions.models import PtSessions
#from .models import 
#from .forms import 

# Create your views here.
def Basket (request):
    
    items = Basket.objects.all()
    itemlines = get_object_or_404(BasketItem)
    template = 'basket/index.html'
    content = {'items':items,
               'itemlines':itemlines }
    return render(request, template,content)