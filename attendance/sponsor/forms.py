from django import forms
from django.contrib.auth.models import User
from .models import Lecturer

class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Employee/Reg No.', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee/Reg No.', 'autofocus': 'True'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class signUpForm(forms.Form):
    username = forms.CharField(max_length=150, label='Employee/Reg No.',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Employee/Reg No.'}))
    email = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'email address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
