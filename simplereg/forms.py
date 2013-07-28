# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'maxlength': 75}), label=_('Email'))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), label=_('Password'))

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_('Email address is already in use. Please supply a different email address.'))
        return self.cleaned_data['email']

    def save(self):
        #login = uuid.uuid4().hex[:30]
        login = self.cleaned_data['email']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = User.objects.create_user(login, email, password)
        user.is_staff = False
        user.save()
        user = authenticate(login=login, email=user.email, passsword=user.password)
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_('Email'), max_length=75)
