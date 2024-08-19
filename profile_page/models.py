from django.db import models
from django.contrib.auth.models import User
from ptsessions.models import PtSessions


class Profile(models.Model):
    username = User.username
    email = User.email
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    your_date_field = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
