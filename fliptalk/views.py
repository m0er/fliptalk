# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt

import fliptalk.services.user as user_service


def index(request):
    return render_to_response('demo.html', context_instance=RequestContext(request))


def demo(request):
    return render_to_response('demo.html', context_instance=RequestContext(request))


@csrf_exempt
def post(request):
    method = request.method
    if method == 'GET':
        return render_to_response('post.html', context_instance=RequestContext(request))
    elif method == 'POST':
        pass


@csrf_exempt
def register(request):
    method = request.method
    if method == 'GET':
        return render_to_response('register.html', context_instance=RequestContext(request))
    elif method == 'POST':
        if 'email' in request.path_info:
            email = request.POST.get('email')
            password = request.POST.get('password')
            nickname = request.POST.get('nickname')
            user_service.register_by_email(request, email, password, nickname)

        return redirect('/demo')


@csrf_exempt
def login(request):
    method = request.method
    if method == 'GET':
        return render_to_response('login.html', context_instance=RequestContext(request))
    elif method == 'POST':
        if 'email' in request.path_info:
            email = request.POST.get('email')
            password = request.POST.get('password')
            result = user_service.login_by_email(request, email, password)

        return redirect('/demo')


def logout(request):
    user_service.logout(request)
    return redirect('/demo')
