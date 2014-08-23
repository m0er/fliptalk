# -*- coding:utf-8 -*-

from fliptalk.const import *
from django.conf import settings
from django.db import models
from django.db.models import Count
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Photo(models.Model):
    uri = models.URLField(blank=False)


# 유저 계정정보
class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=UserManager.normalize_email(email), nickname=nickname)

        if not password:
            user.set_unusable_password()
        else:
            user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(email, nickname, password=password)
        user.isAdmin = True

        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    nickname = models.CharField(max_length=16, unique=True, db_index=True)
    desc = models.CharField(max_length=1000, blank=True)
    dateJoined = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
    isAdmin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def get_account_dict(self):
        account_dict = account_dict()
        account_dict['email'] = self.email
        account_dict['nickname'] = self.nickname
        if self.desc:
            account_dict['desc'] = self.desc
        account_dict['isActive'] = self.isActive
        account_dict['isAdmin'] = self.isAdmin

        return account_dict

    def get_dict(self):
        user_dict = dict()
        user_dict['email'] = self.email
        user_dict['nickname'] = self.nickname
        if self.desc:
            user_dict['desc'] = self.desc

        return user_dict


class UserBackend(object):
    def authenticate(self, username=None, password=None):
        # email login
        if username and password:
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
                else:
                    return None
            except User.DoesNotExist:
                return None

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class Reference(models.Model):
    uri = models.URLField(blank=False)
    count = models.IntegerField(default=0)

class Post(models.Model):
    title = models.CharField(blank=False, max_length=1000)
    summary = models.CharField(blank=True, max_length=1000)
    content = models.TextField(blank=True)
    agreeLabel = models.CharField(blank=True, max_length=100, default=DEFAULT_AGREE_LABEL)
    disagreeLabel = models.CharField(blank=True, max_length=100, default=DEFAULT_DISAGREE_LABEL)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    status = models.SmallIntegerField(default=0)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    references = models.ManyToManyField(Reference, related_name='+')

    def get_dict(self):
        post_dict = dict()
        post_dict['title'] = self.title
        if self.summary:
            post_dict['summary'] = self.summary
        if self.content:
            post_dict['content'] = self.content
        if self.agreeLabel and self.disagreeLabel:
            post_dict['agreeLabel'] = self.agreeLabel
            post_dict['disagreeLabel'] = self.disagreeLabel
        post_dict['writer'] = self.writer.get_dict()
        post_dict['status'] = self.status
        post_dict['createTime'] = self.createTime
        post_dict['updateTime'] = self.updateTime
        if self.references:
            post_dict['references'] = self.references.values()

        return post_dict