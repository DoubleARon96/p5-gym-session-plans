from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from ptsessions.models import PtSessions
import stripe
from basket.contexts import basket_contents
from .models import Order, OrderLineProduct
from .forms import OrderForm

def Checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    items = request.session.get('basket', {})

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'post_code': request.POST['post_code'],
            'town_or_city': request.POST['town_or_city'],
            'first_line_of_address': request.POST['first_line_of_address'],
            'second_line_of_address': request.POST['second_line_of_address'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for session_id, session_data in items.items():
                try:
                    product = PtSessions.objects.get(id=session_id)
                    if isinstance(session_data, int):
                        order_line_item = OrderLineProduct(
                            order=order,
                            product=product,
                            quantity=session_data,
                            line_price_total=product.item_price * session_data  # Use the correct field name
                        )
                        order_line_item.save()
                        return redirect(reverse('basket'))
                    else:
                        for product_id, quantity in session_data.items():
                            order_line_item = OrderLineProduct(
                                order=order,
                                product=product,
                                quantity=quantity,
                                line_price_total=product.item_price * quantity  # Use the correct field name
                            )
                            order_line_item.save()
                except PtSessions.DoesNotExist:
                    messages.error(request, 'Sorry, we could not find this session.')
                    order.delete()
                    return redirect(reverse('basket'))

    else:
        if not items:
            messages.error(request, "You have an empty basket.")
            return redirect(reverse('ptsessions'))

        active_basket = basket_contents(request)
        total = active_basket['grand_total']
        stripe_cost = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_cost,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()
        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. Did you forget to set it?')

        template = 'payments/index.html'
        context = {
            'order_form': order_form,
            'basket': items,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }
        return render(request, template, context)