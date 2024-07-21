from django.db import models
from django.contrib.auth.models import User
from ptsessions.models import PtSessions
# Create your models here.

class BasketItem(models.Model):
    """
    This will make the basket line item
    """
    basket = models.ForeignKey('Basket', on_delete=models.CASCADE)
    product = models.ForeignKey(PtSessions, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.product.session_name}"
    
class Basket(models.Model):
    """
    This makes the data for the total and all products added to it
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(PtSessions, through='BasketItem')

    def __str__(self):
        return f"Basket for {self.user.username}"
