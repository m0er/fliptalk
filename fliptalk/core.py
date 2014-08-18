# -*- coding:utf-8 -*-
import json
import math
import datetime
import re
import random

import requests
from django.contrib.auth import logout
from django.utils import timezone
from django.conf import settings
from django.http import HttpResponse

from fliptalk.const import *
from fliptalk.error import *


class DjangoJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S')
        try:
            return json.JSONEncoder.default(self, obj)
        except:
            return None


def time_to_string(time, format='%Y/%m/%d %H:%M:%S'):
    return time.strftime(format)


def string_to_time(str, format='%Y/%m/%d %H:%M:%S'):
    tzNow = timezone.now()
    return tzNow.strptime(str, format).replace(tzinfo=tzNow.tzinfo)


def join_id_list(list, pattern=','):
    retString = ''
    index = 0
    for id in list:
        retString += str(id)
        if index + 1 < len(list):
            retString += pattern
        index += 1

    return retString


def split_string(string, pattern=','):
    retArray = []
    if string == '':
        return retArray
    stringArray = string.split(pattern)
    for str in stringArray:
        retArray.append(str)

    return retArray


def split_id_string(idString, pattern=','):
    stringArray = idString.split(pattern)
    idArray = []
    for id in stringArray:
        try:
            id = int(id)
            idArray.append(id)
        except:
            pass

    return idArray


def split_id_string_to_dict(idString, pattern=','):
    stringArray = idString.split(pattern)
    idDict = {}
    for id in stringArray:
        try:
            id = int(id)
            idDict[id] = id
        except:
            pass

    return idDict


def get_device_and_version(request):
    userAgent = request.META['HTTP_USER_AGENT']
    array = split_string(userAgent, '/')

    deviceName = 'unknown'
    version = '0'

    if len(array) < 2:
        return 'unknown', '0'

    if array[0] == 'Zibit_iOS':
        deviceName = 'ios'
    elif array[0] == 'Zibit_Android':
        deviceName = 'android'

    version = array[1]
    return deviceName, version


def convert_ios_version_to_int(versionStr):
    array = split_string(versionStr, '.')
    if len(array) < 3:
        return 0
    versionInt = int(array[0]) * 100000000 + int(array[1]) * 10000 + int(array[2])
    return versionInt


def is_gte_version(deviceName, deviceVersion, minIosVer, minAndVer):
    if deviceName == 'ios' and convert_ios_version_to_int(deviceVersion) >= convert_ios_version_to_int(minIosVer):
        return True
    elif deviceName == 'android' and int(deviceVersion) >= int(minAndVer):
        return True

    return False


def is_gt_version(deviceName, deviceVersion, minIosVer, minAndVer):
    if deviceName == 'ios' and convert_ios_version_to_int(deviceVersion) > convert_ios_version_to_int(minIosVer):
        return True
    elif deviceName == 'android' and int(deviceVersion) > int(minAndVer):
        return True

    return False


def is_lte_version(deviceName, deviceVersion, minIosVer, minAndVer):
    if deviceName == 'ios' and convert_ios_version_to_int(deviceVersion) <= convert_ios_version_to_int(minIosVer):
        return True
    elif deviceName == 'android' and int(deviceVersion) <= int(minAndVer):
        return True

    return False


def is_lt_version(deviceName, deviceVersion, minIosVer, minAndVer):
    if deviceName == 'ios' and convert_ios_version_to_int(deviceVersion) < convert_ios_version_to_int(minIosVer):
        return True
    elif deviceName == 'android' and int(deviceVersion) < int(minAndVer):
        return True

    return False


def make_zibit_uri(scheme, targetId=None):
    uri = 'zibit://%s' % (scheme,)
    if targetId != None:
        uri = '%s/%d' % (uri, targetId,)

    return uri


def json_str_to_obj(jsonStr):
    obj = json.loads(jsonStr)
    return obj


def json_obj_to_str(jsonObj):
    str = json.dumps(jsonObj)
    return str


def is_user_login(request):
    if request.user.is_authenticated():
        if request.user.is_active:
            return True
        else:
            logout(request)
    return False


def get_json_response(container):
    jsonStr = json.dumps(container, cls=DjangoJSONEncoder)
    return HttpResponse(jsonStr, content_type='application/javascript; charset=utf8')


def get_json_success_response(info=None, infoKey=None, nextRequestKey=None):
    retDict = {"result": "success"}
    if info != None:
        if infoKey != None:
            info = {infoKey: info}
        if nextRequestKey != None:
            info['nextRequestKey'] = nextRequestKey
        retDict['info'] = info

    jsonStr = json.dumps(retDict, cls=DjangoJSONEncoder)
    return HttpResponse(jsonStr, content_type='application/javascript; charset=utf8')


def get_json_failed_response(errorCode, info=None):
    retDict = {"result": "failed", "error": get_error_message_ko(errorCode), "errorCode": errorCode}
    if info != None:
        retDict['info'] = info
    jsonStr = json.dumps(retDict, cls=DjangoJSONEncoder)
    return HttpResponse(jsonStr, content_type='application/javascript; charset=utf8')


def get_json_maintanence_response(messageDict):
    retDict = {"result": "maintenance", "info": messageDict}
    jsonStr = json.dumps(retDict, cls=DjangoJSONEncoder)
    return HttpResponse(jsonStr, content_type='application/javascript; charset=utf8')


def get_json_need_login_response():
    retDict = {"result": "needlogin", "error": get_error_message_ko(Error.NEED_LOGIN), "errorCode": Error.NEED_LOGIN}
    jsonStr = json.dumps(retDict, cls=DjangoJSONEncoder)
    return HttpResponse(jsonStr, content_type='application/javascript; charset=utf8')


def get_last_id_key_from_list(list, count):
    try:
        listLen = len(list)
        if listLen != 0 and listLen >= count:
            retKey = str(list[listLen - 1]['id'])
        else:
            return None
    except:
        return None
    return retKey


def get_last_itemId_key_from_list(list, count):
    try:
        listLen = len(list)
        if listLen != 0 and listLen >= count:
            retKey = str(list[listLen - 1]['itemId'])
        else:
            return None
    except:
        return None
    return retKey


def get_info_list_from_queryset(queryset):
    retList = []
    for row in queryset:
        object = row.get_info_dict()
        retList.append(object)

    return retList


def get_item_list_from_itemset_queryset(queryset, includePoint=False):
    from datetime import timedelta

    retList = []
    for row in queryset:
        object = row.item.get_info_dict()
        object['coverPhotoType'] = row.photoType
        if includePoint:
            object['_point_'] = row.point

        # reissue된 아이템
        if row.issueLikeCount > 0:
            currentTime = timezone.now()
            if currentTime < row.issueDate + timedelta(seconds=84200):
                if object['coverPhotoIconType'] != COVER_ICON_TYPE_ZIBITPICK:
                    object['coverPhotoIconType'] = COVER_ICON_TYPE_OLD

        retList.append(object)

    return retList


def get_item_photo_info_list_from_item_queryset(queryset):
    retList = []
    for row in queryset:
        object = row.get_item_photo_info_dict()
        retList.append(object)

    return retList


def get_item_photo_info_list_from_item_dict_list(list):
    retList = []
    for row in list:
        photoDict = {'itemId': row['id'], 'itemName': row['name'], 'photo': row['mainPhoto']}
        retList.append(photoDict)

    return retList


def get_truncated_str(str, truncateLen, truncatePostfix='...'):
    if str == None:
        return ''

    if len(str) <= truncateLen:
        return str

    if truncateLen < len(truncatePostfix):
        return truncatePostfix[:truncateLen]

    retStr = (str[:(truncateLen - len(truncatePostfix))] + truncatePostfix) if len(str) > truncateLen else str
    return retStr


def get_unicode_escape_byte(str):
    if str == None:
        return 0
    return len(str.encode('unicode_escape'))


def get_unicode_escape_truncated_str(str, truncateByte, truncatePostfix='...'):
    if str == None:
        return ''

    encodedStr = str.encode('unicode_escape')
    if len(encodedStr) <= truncateByte:
        return str

    encodedPostfix = truncatePostfix.encode('unicode_escape')
    if truncateByte < len(encodedPostfix):
        return re.sub(r'([^\\])\\(u|$)[0-9a-f]{0,3}$', r'\1', encodedPostfix[:truncateByte]).decode('unicode_escape')

    partialStr = re.sub(r'([^\\])\\(u|$)[0-9a-f]{0,3}$', r'\1',
                        encodedStr[:(truncateByte - len(encodedPostfix))]) + truncatePostfix
    return partialStr.decode('unicode_escape')


def get_random_default_user_cover_photo():
    coverPhotoCount = len(settings.DEFAULT_USER_COVER_PHOTO_IDS)
    if coverPhotoCount == 0:
        return None

    randomIndex = random.randrange(0, coverPhotoCount)
    photoId = settings.DEFAULT_USER_COVER_PHOTO_IDS[randomIndex]

    from zibit.models import Photo

    try:
        photo = Photo.objects.get(id=photoId)
        return photo
    except Photo.DoesNotExist:
        pass

    return None


def Log(level, message):
    print message.encode('utf-8')
    return


def LogDebug(message):
    Log(LOG_DEBUG, message)


def LogInfo(message):
    Log(LOG_INFO, message)


def LogWarn(message):
    Log(LOG_WARN, message)


def LogError(message):
    Log(LOG_ERROR, message)


def LogFatal(message):
    Log(LOG_FATAL, message)

