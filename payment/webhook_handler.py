from django.http import HttpResponse

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
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handelPayment_intent_paymentFailed(self,event):
        '''
        this function handles the what happens when the payment 
        has failed to work form the stripe website
        '''
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)