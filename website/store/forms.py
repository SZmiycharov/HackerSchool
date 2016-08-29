from django.contrib.auth.models import User
from django import forms
from captcha.fields import ReCaptchaField
from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(RegistrationFormUniqueEmail):
    email = forms.EmailField()
    captcha = ReCaptchaField()


class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username', 'password']