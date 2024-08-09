from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MainUserProgram(models.Model):
    BODY_PART = (
        ('Legs', 'Legs'),
        ('Chest', 'Chest'),
        ('Back', 'Back'),
        ('Abs', 'Abs'),
        ('Shoulders', 'Shoulders'),
        ('All Body', 'All Body')
    )

    session_name = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body_part = models.CharField(max_length=40, choices=BODY_PART, default='All Body')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.session_name} | Made by {self.user}"

class UserProgram(models.Model):
    session = models.ForeignKey(MainUserProgram, on_delete=models.CASCADE)
    exercise_name = models.TextField()
    reps = models.IntegerField()
    sets = models.IntegerField()
    weight = models.IntegerField()
    comment = models.TextField(max_length=300)
    def __str__(self):
        return f"{self.reps} x {self.sets} x {self.weight} | Comments {self.comment}"

    
