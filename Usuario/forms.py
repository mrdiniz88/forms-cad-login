from django.contrib.auth.forms import UserCreationForm
from django import forms 

from .models import Usuario


class CadastroForm(UserCreationForm):
    password1 = forms.CharField(
        label='Senha',
        strip=False,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Confirmar Senha',
        strip=False,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    class Meta:
        model = Usuario
        fields = ['username']
        labels = {
            'username': 'Usuário'
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
            })
        }
        
        
class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'Usuário',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label = 'Senha',
        strip=False,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    