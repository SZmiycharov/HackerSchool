from django.contrib.auth.models import User
from django import forms
from captcha.fields import ReCaptchaField
from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.forms import AuthenticationForm
import sys


class RegisterForm(RegistrationFormUniqueEmail):
    email = forms.EmailField()
    photo = forms.FileField()
    captcha = ReCaptchaField(label='')


class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField(label='')

    class Meta:
        model = User
        fields = ['username', 'password']


class UpdateProfile(forms.ModelForm):
    user = ''
    username = ''
    email = ''

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.username = forms.CharField(required=False, initial=self.user.username)
        self.email = forms.EmailField(required=False, initial=self.user.email)
        print >> sys.stderr, self.user.username
        super(UpdateProfile, self).__init__(*args, **kwargs)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user