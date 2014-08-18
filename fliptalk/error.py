# -*- coding:utf-8 -*-

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)


Error = enum(
    'SUCCESS',  # = 0
    'INVALID_PARAMETER',
    'INVALID_EMAIL_FORMAT',
    'DUPLICATED_EMAIL',
    'INVALID_NICKNAME_FORMAT',
    'DUPLICATED_NICKNAME',
    'INVALID_PASSWORD_FORMAT',
    'INVALID_EMAIL_OR_PASSWORD',
    'LOGIN_RESTRICT_BY_ADMIN',
    'NEED_TO_CREATE_ACCOUNT',
    'INVALID_EXTERNAL_ACCESS_TOKEN',  # = 10
    'INCORRECT_PREV_PASSWORD',
    'NOT_REGISTERED_EMAIL',
    'PERMISSION_DENIED',
    'USER_DOES_NOT_EXIST',
    'ITEM_DOES_NOT_EXIST',
    'PHOTO_DOES_NOT_EXIST',
    'TALK_DOES_NOT_EXIST',
    'COMMENT_ITEM_DOES_NOT_EXIST',
    'COMMENT_TALK_DOES_NOT_EXIST',
    'PHOTO_FILE_MISSING',  # = 20
    'PHOTO_SAVE_ERROR',
    'DB_SAVE_ERROR',
    'DB_DELETE_ERROR',
    'EVENT_DOES_NOT_EXIST',
    'INVALID_WEBID_FORMAT',
    'DUPLICATED_WEBID',
    'WEBID_ALREADY_GENERATED',
    'NEED_TO_SET_PASSWORD',
    'DUPLICATED_FACEBOOK',
    'DUPLICATED_TWITTER',  # = 30
    'ALREADY_PURCHASED',
    'INVALID_VERSION_KEY',
    'TOO_SHORT_NICKNAME',
    'EVENT_DOES_NOT_EXIST',
    'COMMENT_EVENT_DOES_NOT_EXIST',
    'BANNER_DOES_NOT_EXIST',
    'MEDIA_DOES_NOT_EXIST',
    'BRANDNAME_DOES_NOT_EXIST',
    'MODELNAME_DOES_NOT_EXIST',  # = 40
    'TAG_DOES_NOT_EXIST',
    'USER_IS_NOT_ACTIVE',
    'NEED_LOGIN',
)


def get_error_message_ko(errorCode):
    if errorCode == Error.SUCCESS:
        return ''
    elif errorCode == Error.INVALID_PARAMETER:
        return '잘못된 요청입니다'
    elif errorCode == Error.INVALID_EMAIL_FORMAT:
        return '이메일 형식이 잘못되었습니다'
    elif errorCode == Error.DUPLICATED_EMAIL:
        return '이미 등록된 이메일입니다'
    elif errorCode == Error.INVALID_NICKNAME_FORMAT:
        return '닉네임 형식이 잘못되었습니다\n (한글, 영어, 숫자, _만 사용가능, 띄워쓰기 불가)'
    elif errorCode == Error.DUPLICATED_NICKNAME:
        return '이미 등록된 닉네임입니다'
    elif errorCode == Error.INVALID_PASSWORD_FORMAT:
        return '비밀번호 형식이 잘못되었습니다'
    elif errorCode == Error.INVALID_EMAIL_OR_PASSWORD:
        return '이메일 혹은 암호를 다시 확인해주세요'
    elif errorCode == Error.LOGIN_RESTRICT_BY_ADMIN:
        return '관리자의 의해 로그인이 제한되었습니다'
    elif errorCode == Error.NEED_TO_CREATE_ACCOUNT:
        return '계정을 생성해야됩니다'
    elif errorCode == Error.INVALID_EXTERNAL_ACCESS_TOKEN:
        return '잘못된 인증정보입니다. 처음부터 다시 진행해주세요'
    elif errorCode == Error.INCORRECT_PREV_PASSWORD:
        return '정확한 현재 암호를 입력해주세요'
    elif errorCode == Error.NOT_REGISTERED_EMAIL:
        return '등록되지 않은 이메일입니다'
    elif errorCode == Error.PERMISSION_DENIED:
        return '권한이 없습니다'
    elif errorCode == Error.USER_DOES_NOT_EXIST:
        return '유저가 존재하지 않습니다'
    elif errorCode == Error.ITEM_DOES_NOT_EXIST:
        return '아이템이 삭제되었습니다'
    elif errorCode == Error.PHOTO_DOES_NOT_EXIST:
        return '사진이 삭제되었습니다'
    elif errorCode == Error.TALK_DOES_NOT_EXIST:
        return '게시물이 삭제되었습니다'
    elif errorCode == Error.COMMENT_ITEM_DOES_NOT_EXIST:
        return '댓글이 삭제되었습니다'
    elif errorCode == Error.COMMENT_TALK_DOES_NOT_EXIST:
        return '댓글이 삭제되었습니다'
    elif errorCode == Error.PHOTO_FILE_MISSING:
        return '첨부된 사진파일이 없습니다'
    elif errorCode == Error.PHOTO_SAVE_ERROR:
        return '사진저장에 실패하였습니다'
    elif errorCode == Error.DB_SAVE_ERROR:
        return '저장하지 못하였습니다'
    elif errorCode == Error.DB_DELETE_ERROR:
        return '삭제하지 못하였습니다'
    elif errorCode == Error.NEED_TO_SET_PASSWORD:
        return '로그인 비밀번호를 설정해야 됩니다'
    elif errorCode == Error.DUPLICATED_FACEBOOK:
        return '이미 다른 계정에 연동된 페이스북 계정입니다'
    elif errorCode == Error.DUPLICATED_TWITTER:
        return '이미 다른 계정에 연동된 트위터 계정입니다'
    elif errorCode == Error.ALREADY_PURCHASED:
        return '이미 응모하였습니다'
    elif errorCode == Error.INVALID_VERSION_KEY:
        return '데이터가 없습니다'
    elif errorCode == Error.TOO_SHORT_NICKNAME:
        return '닉네임이 너무 짧습니다. 2글자 이상 입력해주세요.'
    elif errorCode == Error.COMMENT_EVENT_DOES_NOT_EXIST:
        return '댓글이 삭제되었습니다'
    elif errorCode == Error.BANNER_DOES_NOT_EXIST:
        return '배너가 없습니다'
    elif errorCode == Error.MEDIA_DOES_NOT_EXIST:
        return '미디어가 삭제되었습니다'
    elif errorCode == Error.BRANDNAME_DOES_NOT_EXIST:
        return '브랜드 이름이 없습니다'
    elif errorCode == Error.MODELNAME_DOES_NOT_EXIST:
        return '모델 이름이 없습니다'
    elif errorCode == Error.TAG_DOES_NOT_EXIST:
        return '태그 이름이 없습니다'
    elif errorCode == Error.USER_IS_NOT_ACTIVE:
        return '탈퇴한 유저입니다'
    elif errorCode == Error.NEED_LOGIN:
        return '로그인이 필요합니다'
    return ''


def get_error_code(string):
    return getattr(Error, string)
