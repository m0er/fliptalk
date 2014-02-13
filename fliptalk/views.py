# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.http.response import Http404
from django.template.context import RequestContext
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def demo(request):
    return render_to_response('demo.html', context_instance=RequestContext(request))