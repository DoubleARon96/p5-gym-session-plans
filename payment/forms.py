from django import forms
from .models import Order, OrderLineProduct

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 
                  'country', 'post_code', 'town_or_city',
                  'first_line_of_address', 'second_line_of_address',
                  'county',)
        
    def __init__(self, *args, **kwargs):
        """
        This will add placeholders on the form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number', 
            'country': 'Country',
            'post_code': 'Post Code / Zip Code',
            'town_or_city': 'Town Or City',
            'first_line_of_address': 'First Line Of Address', 
            'second_line_of_address': 'Second Line Of Address',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
