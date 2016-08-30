from django.contrib.auth.models import User
from django import forms
from captcha.fields import ReCaptchaField
from registration.forms import RegistrationFormUniqueEmail, RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
import sys
from django.views.generic.edit import UpdateView


class RegisterForm(RegistrationFormUniqueEmail):
    email = forms.EmailField()
    captcha = ReCaptchaField(label='')


class UpdateProfileForm(RegistrationForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput(), label="New password")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirm new password")
    captcha = ReCaptchaField(label='')

    class Meta:
        model = User
        exclude = ('last_login', 'is_superuser', 'groups',
                   'user_permissions', 'is_staff', 'is_active', 'date_joined', 'password', 'first_name', 'last_name')


class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField(label='')

    class Meta:
        model = User
        fields = ['username', 'password']

