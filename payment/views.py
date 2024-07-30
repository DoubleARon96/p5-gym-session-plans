from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from basket.contexts import basket_contents
from .forms import OrderForm

import stripe

# Create your views here.

def Checkout (request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    items = request.session.get('basket',{})

    if not items:
        messages.error(request, "You have a Empty Basket")
        #return redirect(reverse('ptsessions'))
    active_basket = basket_contents(request)
    total = active_basket['grand_total']
    stripe_cost = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount = stripe_cost,
        currency = settings.STRIPE_CURRENTCY,
    )

    order_form = OrderForm()
    if not stripe_public_key:
        messages.warning(request,'Stripe Public Key Is Missing, Did You Forget To Set It')

    template = 'payments/index.html'
    content = {
        'order_form': order_form,
        'basket': items,
        'stripe_public_key': stripe_public_key,
        'client_secret' : intent.client_secret,
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

