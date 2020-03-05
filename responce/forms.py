from django import forms
from responce.models import Responce

class Responce(forms.ModelForm): 
    class Meta:
        model = Responce
        fields = ['name', 'email', 'site_url', 'comment']
