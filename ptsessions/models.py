from django.db import models
from django.contrib.auth.models import User


class PtSessions(models.Model):
    BODY_PART = (
        ('Legs', 'Legs'),
        ('Chest', 'Chest'),
        ('Back', 'Back'),
        ('Abs', 'Abs'),
        ('Shoulders', 'Shoulders'),
        ('All Body', 'All Body')
    )
    session_name = models.TextField(max_length=30,
                                    null=False, blank=False)
    program = models.TextField(max_length=4000)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=False, blank=False,
                             related_name='user_sessions')
    body_part = models.CharField(max_length=40,
                                 null=False, blank=False,
                                 choices=BODY_PART, default='All Body')
    client = models.ManyToManyField(User, blank=True,
                                    related_name='client_sessions')
    item_price = models.DecimalField(max_digits=6,
                                     decimal_places=2, null=False,
                                     blank=False, default=0)

    def __str__(self):
        return f"{self.session_name} Cost £{self.item_price}"


class Price(models.Model):
    host_product = models.ForeignKey(PtSessions, on_delete=models.CASCADE)
    price_in_pounds = models.PositiveIntegerField()

    def __str__(self):
        return f"Price for {self.host_product.session_name}"
