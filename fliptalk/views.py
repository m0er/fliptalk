# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
import requests, simplejson, fliptalk.user as userService
from django.http.response import Http404
from django.template.context import RequestContext
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

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
			userService.registerByEmail(request, email, password, nickname)

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
			result = userService.loginByEmail(request, email, password)
		
		return redirect('/demo')

def logout(request):
	userService.logout(request)
	return redirect('/demo')