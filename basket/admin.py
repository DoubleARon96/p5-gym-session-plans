from django.contrib import admin
from .models import BasketItem,Basket

# Register your models here.
admin.site.register(BasketItem)
admin.site.register(Basket)