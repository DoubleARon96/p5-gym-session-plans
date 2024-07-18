from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import BasketItem, Basket
from ptsessions.models import PtSessions
#from .models import 
#from .forms import 

# Create your views here.
def basket_view(request):
    
    items = Basket.objects.all()
    itemlines = BasketItem.objects.all()
    ptsessions = PtSessions.objects.all()
    price = PtSessions.item_price
    title = "Basket"
    template = 'basket/index.html'
    content = {'items':items,
               'price': price,
               'itemlines': itemlines,
                'title': title }
    return render(request, template,content)