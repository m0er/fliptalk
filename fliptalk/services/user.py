# -*- coding:utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from fliptalk.core import *
from fliptalk.const import *
from fliptalk.models import *


@csrf_exempt
def register_by_email(request, email, password, nickname):
    # check param exist
    if not nickname or not password or not email:
        return get_json_failed_response(Error.INVALID_PARAMETER)

    user = User.objects.create_user(email, nickname, password)
    user.save()

    user = authenticate(username=email, password=password)
    login(request, user)

    return get_json_success_response(info=user.getAccountDict(), infoKey='account')


def logoutUser(request):
    logout(request)

    return get_json_success_response()


def login_by_email(request, email, password):
    if not email or not password:
        return get_json_failed_response(Error.INVALID_PARAMETER)

    user = authenticate(username=email, password=password)

    if not user:
        return get_json_failed_response(Error.INVALID_EMAIL_OR_PASSWORD)

    # 탈퇴한 유저
    if not user.is_active:
        return get_json_failed_response(Error.INVALID_EMAIL_OR_PASSWORD)

    login(request, user)

    return get_json_success_response(info=user.getAccountDict(), infoKey='account')