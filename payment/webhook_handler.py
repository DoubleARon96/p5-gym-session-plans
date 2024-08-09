from django.http import HttpResponse

from basket.contexts import basket_contents
from .models import Order, OrderLineProduct
from ptsessions.models import PtSessions

import stripe
import json
import time

class stripeWeb_handler:
    '''
    this class will listen to stripe
    '''
    def __init__(self,request):
        self.request=request
    
    def handelEvent(self,event):
        '''
        this function handles the events
        '''

        return HttpResponse(
            content=f'unhandled Webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        '''
        This function handles what happens when the payment is
        successful from the Stripe website.
        '''
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=shipping_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    post_code__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    first_line_of_address__iexact=shipping_details.address.line1,
                    second_line_of_address__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_basket=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | Success: Verified order in database',
                status=200
            )
        else:
            order = None
            try:
                for session_id, session_data in json.loads(bag).items():
                    order = Order.objects.create(
                        full_name=shipping_details.name,
                        email=shipping_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        post_code=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        first_line_of_address=shipping_details.address.line1,
                        second_line_of_address=shipping_details.address.line2,
                        county=shipping_details.address.state,
                        original_basket=bag,
                        stripe_pid=pid,
                    )
                    product = PtSessions.objects.get(id=session_id)
                    if isinstance(session_data, int):
                        order_line_item = OrderLineProduct(
                            order=order,
                            product=product,
                            quantity=session_data,
                            line_price_total=product.item_price * session_data
                        )
                        order_line_item.save()
                    else:
                        for product_id, quantity in session_data.items():
                            order_line_item = OrderLineProduct(
                                order=order,
                                product=product,
                                quantity=quantity,
                                line_price_total=product.item_price * quantity
                            )
                            order_line_item.save()
            except Exception as e:
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | Error: {str(e)}',
                    status=500
                )

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | Success: Created order in webhook',
            status=200
        )

    def handelPayment_intent_paymentFailed(self,event):
        '''
        this function handles the what happens when the payment 
        has failed to work form the stripe website
        '''
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)