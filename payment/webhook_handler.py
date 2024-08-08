from django.http import HttpResponse
from .models import Order, OrderLineProduct
from ptsessions.models import PtSessions

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
    
    def handelPayment_intentSucceeded(self,event):
        '''
        this function handles the what happens when the payment is
        successful form the stripe website
        '''
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2) # updated

        for fields, value in shipping_details.address.items():
            if value == "":
                shipping_details.address['']=None
        
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.full_name,
                    email__iexact=shipping_details.email,
                    phone_number__iexact=shipping_details.phone_number,
                    country__iexact=shipping_details.country,
                    post_code__iexact=shipping_details.post_code,
                    town_or_city__iexact=shipping_details.town_or_city,
                    first_line_of_address__iexact=shipping_details.first_line_of_address,
                    second_line_of_address__iexact=shipping_details.second_line_of_address,
                    county__iexact=shipping_details.county,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
                
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
            if order_exists:
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | Success Verfied Order In Database',
                        status=200)
            else:
                order=None     
                try:
                    for session_id, session_data in json.loads(basket).items():
                        order = Order.object.create(
                        full_name_shipping_details.full_name,
                        email_shipping_details.email,
                        phone_number_shipping_details.phone_number,
                        country_shipping_details.country,
                        post_code_shipping_details.post_code,
                        town_or_city_shipping_details.town_or_city,
                        first_line_of_address_shipping_details.first_line_of_address,
                        second_line_of_address_shipping_details.second_line_of_address,
                        county_shipping_details.county,
                        original_basket=basket,
                        stripe_pid=pid,
                        )
                    product = PtSessions.objects.get(id=session_id)
                    if isinstance(session_data, int):
                        order_line_item = OrderLineProduct(
                            order=order,
                            product=product,
                            quantity=session_data,
                            line_price_total=product.item_price * session_data  # Use the correct field name
                        )
                        order_line_item.save()
                    else:
                        for product_id, quantity in session_data.items():
                            order_line_item = OrderLineProduct(
                            order=order,
                            product=product,
                            quantity=quantity,
                            line_price_total=product.item_price * quantity  # Use the correct field name
                            )
                            order_line_item.save()
                except Exception as e:
                    if order:
                        order.delete()
                        return HttpResponse(
                            content=f'Webhook received: {event["type"]} | ERROR:{e}',
                            status=500)

            
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS Created Order In Webhook',
                status=200)

    def handelPayment_intent_paymentFailed(self,event):
        '''
        this function handles the what happens when the payment 
        has failed to work form the stripe website
        '''
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)