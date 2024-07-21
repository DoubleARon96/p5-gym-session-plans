from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from basket.models import BasketItem, Basket

from .forms import OrderForm

# Create your views here.

def Checkout (request):
    items = request.session.get(' Basket',{})
    if not items:
        messages.error(request, "You have a Empty Basket")
        return redirect(reverse('basket'))
    order_form = OrderForm()
    template = 'payment/index.html'
    content = {
        'order_form': order_form
    }
    return render(request, template, content)