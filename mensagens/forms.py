from django import forms
from .models import Mensagens

class MensagensForm(forms.ModelForm):
    class Meta:
        model = Mensagens
        fields = ['nome', 'texto']
