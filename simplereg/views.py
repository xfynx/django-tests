# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.contrib.auth import login
from simplereg.forms import *


def registration(request, template_name='registration.html',
                 form_class=RegForm, extra_context=None,
                 callback=None, autologin=True):
    form = form_class(request.POST or None)
    if form.is_valid():

        user = form.save()

        if autologin:
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            #user = authenticate(email=email, password=password)
            login(request, user)

        if callback:
            callback(request, user)

        return redirect('/polls/login/')

    context = {
        'form': form
    }
    context.update(extra_context or {})
    return TemplateResponse(request, template_name, context)
