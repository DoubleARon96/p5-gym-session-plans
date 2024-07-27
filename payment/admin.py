from django.contrib import admin
from .models import Order, OrderLineProduct


class OrderLineProductAdminInline(admin.TabularInline):
    model = OrderLineProduct
    readonly_fields =('line_price_total',)

class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineProductAdminInline,)

    readonly_fields =('order_number','date',
                      'product_total', 'total',)
    
    fields = ('order_number', 'full_name', 'email', 'phone_number', 
              'country', 'post_code', 'town_or_city',
              'first_line_of_address', 'second_line_of_address',
              'county', 'date', 'product_total', 'total',)
    
    list_display = ('order_number', 'date', 'total',)
    ordering = ('-date',)

    from .models import OrderLineProduct

admin.site.register(Order,OrderAdmin)