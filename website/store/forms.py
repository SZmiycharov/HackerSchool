from django.contrib.auth.models import User
from django import forms
from captcha.fields import ReCaptchaField
from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.forms import AuthenticationForm


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


class UpdateProfile(RegistrationFormUniqueEmail):
    email = forms.EmailField()
    photo = forms.FileField()
    captcha = ReCaptchaField(label='')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(RegistrationFormUniqueEmail, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user