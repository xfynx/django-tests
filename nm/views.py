import os

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import *

from nm.models import Choice, Poll

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))


# def home(request):
#     username = get_user(request)
#     return render(request, 'templates/home.html', {'username': username})


def user_login(request):
    username = get_user(request)
    return render(request, 'templates/loginfo.html', {'username': username})


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'templates/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('nm:results', args=(p.id,)))


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'templates/detail.html', {'poll': poll})