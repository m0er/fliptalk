# -*- coding:utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from fliptalk.view_helper import *
from fliptalk.models import *
from fliptalk.error import *


@csrf_exempt
def register_by_email(request, email, password, nickname):
    # check param exist
    if not nickname or not password or not email:
        return JsonResponseError({'code': 400, 'msg': get_error_message(Error.INVALID_PARAMETER)})

    user = User.objects.create_user(email, nickname, password)
    user.save()

    user = authenticate(username=email, password=password)
    login(request, user)

    return JsonResponse({'user': user.get_dict()})

def logout_user(request):
    logout(request)

    return JsonResponse()


def login_by_email(request, email, password):
    if not email or not password:
        return JsonResponseError({'code': 400, 'msg': get_error_message(Error.INVALID_PARAMETER)})

    user = authenticate(username=email, password=password)

    if not user:
        return JsonResponseError({'code': 400, 'msg': get_error_message(Error.INVALID_EMAIL_OR_PASSWORD)})

    # 탈퇴한 유저
    if not user.is_active:
        return JsonResponseError({'code': 400, 'msg': get_error_message(Error.INVALID_EMAIL_OR_PASSWORD)})

    login(request, user)

    return JsonResponse({'user': user.get_dict()})