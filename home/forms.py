from django import forms
from .models import HomeNews


class NewsForm (forms.ModelForm):
    class Meta:
        model = HomeNews
        fields = '__all__'

        labels = {
            'title':'Title',
            'content':'Content'
        }

        widgets  ={
            'title' : forms.TextInput(attrs={'placeholder': 'eg. Welcome'}),
            'content' : forms.TextInput(attrs={'placeholder': 'eg. lets begin a story'}),
        }