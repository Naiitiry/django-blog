from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Formulario de Registro
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }
        help_texts = {
            'username':'',
            'email':'',
            'password1':'',
            'password2':'',
        }

class LoginForm(forms.Form):
    username = forms.CharField(
    widget=forms.TextInput(attrs={'class':'form-control'}),
    label="Usuario"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label="Contraseña"
    )