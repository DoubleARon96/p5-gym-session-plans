from django import forms
from .models import MainUserProgram,UserProgram

class UserSessionsForm (forms.ModelForm):
    class Meta:
        model = UserProgram
        fields = ('session','exercise_name','reps','sets','weight','comment')


class MainUserProgramForm (forms.ModelForm):
    class Meta:
        model = MainUserProgram
        fields = ('user','session_name','body_part',)
