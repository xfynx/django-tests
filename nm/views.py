import os

from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from nm.models import *


PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'templates/index.html', context)


def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'templates/detail.html', {'poll': poll})