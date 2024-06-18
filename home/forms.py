from django import forms
from .models import HomeNews



class NewsForm (forms.ModelForm):
    class Meta:
        model = HomeNews
        fields = '__all__'

        labels = {
            'id': 'Identification',
            'title':'Title',
            'content':'Content'
        }