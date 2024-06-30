from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    #user image
    username = User.username
    email = User.email
    date_of_birth = models.DateField()
    def __str__(self):
        return self.username