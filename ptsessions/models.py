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
    session_name = models.TextField(max_length=30, null=False, blank=False)
    program = models.TextField(max_length=4000)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=False, blank=False, related_name='user_sessions')
    body_part = models.CharField(max_length=40,null=False, blank=False, choices=BODY_PART, default='All Body')
    client = models.ForeignKey(User, on_delete=models.CASCADE,null=False, blank=False, related_name='client_sessions')
    price_in_pounds = models.PositiveIntegerField()
    # Add other fields as needed

    def __str__(self):
        return f"{self.session_namereturn} Price = {self.host_product.price}"
