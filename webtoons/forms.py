# webtoons/forms.py
from django import forms
from .models import Webtoon

class WebtoonForm(forms.ModelForm):
    class Meta:
        model = Webtoon
        fields = ['titulo', 'autor', 'descricao', 'capa', 'status']
        # Opcional: Adicionar classes CSS para estilizar os campos
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-input'}),
            'autor': forms.TextInput(attrs={'class': 'form-input'}),
            'descricao': forms.Textarea(attrs={'class': 'form-textarea'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }