from django import forms
from django.forms  import ModelForm
from .models import RegistrationData
class RegistrationForm(forms.Form):
    user=forms.CharField(max_length=15,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'username'
    }))
    password=forms.CharField(max_length=15,widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'password'
    }))
    email=forms.CharField(max_length=15,widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'email'
    }))
    phone=forms.CharField(max_length=15,widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'phone'
    }))


class RegistrationModal(forms.ModelForm):

    class Meta:
        model = RegistrationData

        fields = [
            'user',
            'password',
            'email',
            'phone'
        ]
        widgets = {
            'user':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'username'
                }),
            'password':forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'password'
        }),
            'email':forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'email'
        }),
            'phone':forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'phone'
        })
        }
