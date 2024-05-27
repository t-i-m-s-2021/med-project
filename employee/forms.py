from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from employee.models import Employee

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин', 'class': 'authbox'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'authbox'}))

    class Meta:
        model = Employee
        fields = ['username', 'password']

class RegisterForm(UserCreationForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите ФИО'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))
    is_admin = forms.BooleanField(required=False)


    class Meta:
        model = Employee
        fields = ['fullname', 'password1', 'password2', 'username', 'is_admin']