from django import forms
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import CustomerUser
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput
from django.shortcuts import redirect


def regis_isvalid(request):
    if form.is_valid():
        form.save()
        return redirect('login')


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=13, label='Phone number')
    birth_date = forms.DateField(label="Birth date", widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CustomerUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'birth_date', 'image_user', 'password1', 'password2')
        labels = {
            'first_name': "Ism",
            'last_name': "Familiya",
            'username': "Login",
            'email': "Email",
            'phone_number': "Telefon raqam",
            'birth_date': "Tug'ilgan kun",
            'image_user': "Profil uchun rasm"

        }


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class CustomerUserUpdateForm(ModelForm):
    class Meta:
        model = CustomerUser
        fields = ['username', 'first_name', 'last_name', 'email', 'image_user', 'phone_number', 'birth_date',
                  'password']
        labels = {
            'first_name': "Ism",
            'last_name': "Familiya",
            'username': "Login",
            'email': "Email",
            'phone_number': "Telefon raqam",
            'birth_date': "Tug'ilgan kun",
            'image_user': "Profil uchun rasm"

        }