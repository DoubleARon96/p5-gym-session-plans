from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def Checkout (request):
    items = request.session.get('basket',{})
    if not items:
        messages.error(request, "You have a Empty Basket")
        return redirect(reverse('ptsessions'))
    order_form = OrderForm()
    template = 'payment/index.html'
    content = {
        'order_form': order_form
    }
    return render(request, template, content)