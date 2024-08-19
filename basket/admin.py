from django.contrib import admin
from .models import BasketItem, Basket

'''
this will register my admin models
'''
admin.site.register(BasketItem)
admin.site.register