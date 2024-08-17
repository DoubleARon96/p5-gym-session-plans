from django.shortcuts import render, get_object_or_404,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from .models import BasketItem, Basket
from ptsessions.models import PtSessions
#from .models import 
#from .forms import 


@login_required
def basket_view(request):
    items = Basket.objects.filter(user=request.user)
    title = "Basket"
    template = 'basket/index.html'
    content = {'items':items,
                'title': title,
                'user': request.user,
                }
    return render(request, template,content)

def add_to_basket(request, session_id=id):
    """ 
    Add a quantity of the specified product to the basket
    """

    basket = request.session.get('basket', {})

    request.session.get('basket', {})
    if session_id in basket:
        basket[session_id] += 1  
    else:
        basket[session_id] = 1  
    request.session['basket'] = basket
    messages.success(request, f'Product Was Added')
    return redirect('ptsessions')

def adjust_basket(request, session_id=id):
    """ 
     delete a specified product from the basket
    """
    quantity_str = request.POST.get('quantity')
    basket = request.session.get('basket', {})
    try:
        quantity = int(quantity_str)
    except (ValueError, TypeError):
        quantity = 1

    request.session.get('basket', {})
    if quantity > 0:
        basket[session_id] = basket.get(session_id, 0)
        
    else:
        basket.pop (session_id, None)

    request.session['basket']=basket
    return redirect('basket')
    