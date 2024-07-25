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
    title = "Basket"
    template = 'basket/index.html'
    content = {'items':items,
                'title': title,
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
        basket.pop (session_id)
    request.session['basket']=basket
    return redirect('basket')
    