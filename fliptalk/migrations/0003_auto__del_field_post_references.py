# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.references'
        db.delete_column(u'fliptalk_post', 'references_id')

        # Adding M2M table for field references on 'Post'
        m2m_table_name = db.shorten_name(u'fliptalk_post_references')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm[u'fliptalk.post'], null=False)),
            ('reference', models.ForeignKey(orm[u'fliptalk.reference'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'reference_id'])


    def backwards(self, orm):
        # Adding field 'Post.references'
        db.add_column(u'fliptalk_post', 'references',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=datetime.datetime(2014, 2, 22, 0, 0), related_name='+', to=orm['fliptalk.Reference']),
                      keep_default=False)

        # Removing M2M table for field references on 'Post'
        db.delete_table(db.shorten_name(u'fliptalk_post_references'))


    models = {
        u'fliptalk.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uri': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'fliptalk.post': {
            'Meta': {'object_name': 'Post'},
            'agreeLabel': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'createTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'disagreeLabel': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'references': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': u"orm['fliptalk.Reference']"}),
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