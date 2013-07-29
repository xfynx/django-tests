# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, logout
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'maxlength': 75}), label=_('Email/login'))
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
        user = authenticate(login=login, email=email, password=password)
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_('Email/login'), max_length=75)


def log_out(request):
    logout(request)
    # redirect_to = request.REQUEST.get(redirect_field_name, '')
    # if redirect_to:
    #     netloc = urlparse.urlparse(redirect_to)[1]
    #     # Security check -- don't allow redirection to a different host.
    #     if not (netloc and netloc != request.get_host()):
    return redirect('/polls/home')