# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from fliptalk.models import *
import fliptalk.user as user_service


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


def demo(request):
    return render_to_response('demo.html', context_instance=RequestContext(request))

def list(request):
    posts = Post.objects.all()
    return render_to_response('list.html', {
        'posts': posts
    }, context_instance=RequestContext(request))

def get_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render_to_response('post.html', {
        'post': post
    }, context_instance=RequestContext(request))

@csrf_exempt
def post_form(request):
    method = request.method
    if method == 'GET':
        return render_to_response('post_form.html', context_instance=RequestContext(request))
    elif method == 'POST':
        if not request.user.is_authenticated():
            redirect('/login/email')

        title = request.POST.get('title')
        summary = request.POST.get('summary')
        content = request.POST.get('content')
        reference = request.POST.get('reference')
        user = request.user

        goc_reference, created = Reference.objects.get_or_create(uri=reference)
        if goc_reference:
            goc_reference.count += 1
            goc_reference.save()

        new_post = Post(title=title, summary=summary, content=content, writer=user)
        new_post.save()

        new_post.references.add(goc_reference)
        new_post.save()

        return redirect('/')

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
            print result

        return redirect('/demo')


def logout(request):
    user_service.logout_user(request)
    return redirect('/demo')
