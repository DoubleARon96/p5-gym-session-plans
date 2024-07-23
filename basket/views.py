from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from .models import BasketItem, Basket
from ptsessions.models import PtSessions
#from .models import 
#from .forms import 


@login_required
#@permission_required('basket.view_basket', raise_exception=True)
def basket_view(request):
    items = Basket.objects.filter(user=request.user)
    itemlines = BasketItem.objects.filter(basket__in=items)
    ptsessions = PtSessions.objects.all()
    price = PtSessions.item_price
    title = "Basket"
    template = 'basket/index.html'
    content = {'items':items,
               'price': price,
               'itemlines': itemlines,
                'title': title,
                'ptsessions': ptsessions,
                'user': request.user,
                }
    return render(request, template,content)

def delete_item(request, id):
    queryset =  get_object_or_404 (BasketItem, id=id)
    if request.method == 'POST':
        queryset.delete()
        return redirect('basket')
    else:
         messages.error(request, "Exercise couldn't be deleted!")
    
    return render (request, "userprograms/userprograms/delete-failed.html")