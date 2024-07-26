from django.db import models
from django.db.models import Sum
from django.conf import settings
from ptsessions.models import PtSessions
from basket.models import BasketItem, Basket
import uuid

# Create your models here.
class Order (models.Model):
    order_number = models.CharField(max_length=32, editable=False, unique=True)
    full_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=300, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=50, null=True, blank=False)
    post_code = models.CharField(max_length=10, null=True, blank=False)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    first_line_of_address = models.CharField(max_length=80, null=False, blank=False)
    second_line_of_address = models.CharField(max_length=80, null=True, blank=False)
    county = models.CharField(max_length=50, null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    product_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        this will make a order number using UUID
        """
        return uuid.uuid4().hex.upper()
    
    #def update_total(self):
        """
        this function will add up the total of 
        each product line
        """
        #self.total = self.BasketItem.aggregate(sum('basket_items'))['total__sum']
       # if self.total == self.product_total :
        #    self.save
    
    
    def save(self, *args, **kwargs):
        """
        this function over writes the save method to set a order number
        that hasn't been used already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.order_number

class OrderLineProduct(models.Model):
    order = models.ForeignKey(Basket, null=False, blank=False, on_delete=models.CASCADE, related_name="product_lines")
    product = models.ForeignKey(PtSessions, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    #access key?
    #access code?
    line_price_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        this function over writes the save method and sets line price total
        and updates the total
        """
        self.line_price_total = self.product.item_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Program Title {self.product.session_name} with Order Number {self.order.order_number}'