from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import PtSessions,Price
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

def Add_to_basket (request, Ptsessions):
    item = get_object_or_404(PtSessions, id=Ptsessions)
    basket, created = Basket.objects.get_or_create(user=request.user) 

    item_in_basket, item_created = BasketItem.objects.get_or_create(user_basket=basket, item=item)
    if not item_created:
        #item_in_basket.quantity += 1
        item_in_basket.save()
        
    return redirect('ptsessions')
