from django import forms
from .models import MainUserProgram,UserProgram

class UserSessionsForm (forms.ModelForm):
    class Meta:
        model = UserProgram
        fields = ('exercise_name','reps','sets','weight','comment')

    def __init__(self, *args, **kwargs):
        self.session = kwargs.pop('session', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.session:
            instance.session = self.session
        if commit:
            instance.save()
        return instance


class MainUserProgramForm (forms.ModelForm):
    class Meta:
        model = MainUserProgram
        fields = ('session_name','body_part',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance
