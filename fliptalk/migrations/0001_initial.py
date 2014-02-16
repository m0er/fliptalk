# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'fliptalk_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=255, db_index=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16, db_index=True)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('dateJoined', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('isActive', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('isAdmin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'fliptalk', ['User'])

        # Adding model 'Photo'
        db.create_table(u'fliptalk_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'fliptalk', ['Photo'])

        # Adding model 'Reference'
        db.create_table(u'fliptalk_reference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uri', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'fliptalk', ['Reference'])

        # Adding model 'Post'
        db.create_table(u'fliptalk_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('actionLabel', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('writer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['fliptalk.User'])),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('createTime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updateTime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('references', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['fliptalk.Reference'])),
        ))
        db.send_create_signal(u'fliptalk', ['Post'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'fliptalk_user')

        # Deleting model 'Photo'
        db.delete_table(u'fliptalk_photo')

        # Deleting model 'Reference'
        db.delete_table(u'fliptalk_reference')

        # Deleting model 'Post'
        db.delete_table(u'fliptalk_post')


    models = {
        u'fliptalk.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'fliptalk.post': {
            'Meta': {'object_name': 'Post'},
            'actionLabel': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'createTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'references': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['fliptalk.Reference']"}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'updateTime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'writer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['fliptalk.User']"})
        },
        u'fliptalk.reference': {
            'Meta': {'object_name': 'Reference'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'fliptalk.user': {
            'Meta': {'object_name': 'User'},
            'dateJoined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isActive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'isAdmin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'nickname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16', 'db_index': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['fliptalk']