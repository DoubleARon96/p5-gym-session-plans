from django.db import models
from django.contrib.auth.models import User
from ptsessions.models import PtSessions

# Create your models here.

class Profile(models.Model):
    #user image
    username = User.username
    email = User.email
    date_of_birth = models.DateField(default= "0/00/0000")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.username
    
