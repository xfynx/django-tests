from django.http import HttpResponse
from django.template import Context, loader
import os
from nm.models import *

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('templates/index.html')
    # path_css = os.path.join(PROJECT_PATH, '/css/test.css')
    context = Context({
        'latest_poll_list': latest_poll_list,
        # 'path_css': path_css
    })
    return HttpResponse(template.render(context))


def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)