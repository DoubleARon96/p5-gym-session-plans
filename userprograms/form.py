from django import forms
from .models import MainUserProgram,UserPrograme

class UserSessionsForm (forms.ModelForm):
    class Meta:
        model = UserPrograme
        fields = ('reps','sets','weight','comment')
