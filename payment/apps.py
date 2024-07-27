from django.apps import AppConfig


#class PaymentConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    #name = 'payment'
class PaymentConfig(AppConfig):
    name = 'payment'

    def ready(self):
        import payment.signals