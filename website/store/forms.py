from django.contrib.auth.models import User
from django import forms
from captcha.fields import ReCaptchaField
from registration.forms import RegistrationFormUniqueEmail, RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm, CharField, TextInput, IntegerField
from .models import Product
import sys


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


class PurchaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        if kwargs.get("product_id", ""):
            print >> sys.stderr, "Buying with product_id"
            product_id = kwargs.pop("product_id")
            product = Product.objects.all().filter(id=product_id)[0]
            maxquantity = getattr(product, 'quantity')
            super(PurchaseForm, self).__init__(*args, **kwargs)
            self.fields['quantity'] = IntegerField(min_value=0, max_value=maxquantity, required=False)
        elif kwargs.get("fromshoppingcart", ""):
            kwargs.pop("fromshoppingcart")
            print >> sys.stderr, "Buying with shopping cart"
            super(PurchaseForm, self).__init__(*args, **kwargs)
            self.fields['quantity'] = IntegerField(disabled=True, required=False)

    address = forms.CharField(label='Address', max_length=100, required=False)
    phonenumber = IntegerField(min_value=0, max_value=999999999999, required=False)
    captcha = ReCaptchaField(label='')








