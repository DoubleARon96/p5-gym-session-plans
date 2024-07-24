from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
import stripe
from basket.models import BasketItem, Basket
from .forms import OrderForm

# Create your views here.

def Checkout (request):
    items = request.session.get('Basket',{})
    if not items:
        messages.error(request, "You have a Empty Basket")
        #return redirect(reverse('basket'))
    order_form = OrderForm
    template = 'payments/index.html'
    content = {
        'order_form': order_form,
        'basket': items,
    }
    return render(request, template, content)

def pay_function(request):  # new
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == "POST":
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": "prod_QXDtoiE5OjOr9F",  # enter yours here!!!
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=request.build_absolute_uri(reverse("success")),
            cancel_url=request.build_absolute_uri(reverse("cancel")),
        )
        return redirect(checkout_session.url, code=303)
    return render(request, "home.html")

def success(request):
    return render(request, "success.html")


def cancel(request):
    return render(request, "cancel.html")

