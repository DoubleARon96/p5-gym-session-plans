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
    session_name = models.TextField()
    program = models.TextField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sessions')
    body_part = models.CharField(max_length=40, choices=BODY_PART, default='All Body')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_sessions')
    # Add other fields as needed

    def __str__(self):
        return self.session_name

class Price(models.Model):
    host_product = models.ForeignKey(PtSessions, on_delete=models.CASCADE)
    price_in_pounds = models.PositiveIntegerField()

    def __str__(self):
        return f"Price for {self.host_product.session_name}"
