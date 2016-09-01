from django.contrib.auth.models import User
from django import forms
from captcha.fields import ReCaptchaField
from registration.forms import RegistrationFormUniqueEmail, RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm, CharField, TextInput, IntegerField


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


class PaymentForm(forms.Form):
    address = forms.CharField(label='Address', max_length=100)
    phonenumber = IntegerField(min_value=0, max_value=9999999999999)
    quantity = IntegerField(min_value=0, max_value=10)
    captcha = ReCaptchaField(label='')





