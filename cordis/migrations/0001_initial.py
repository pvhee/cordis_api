# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'cordis_project', (
            ('rcn', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('data', self.gf('picklefield.fields.PickledObjectField')(null=True)),
        ))
        db.send_create_signal(u'cordis', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'cordis_project')


    models = {
        u'cordis.project': {
            'Meta': {'object_name': 'Project'},
            'data': ('picklefield.fields.PickledObjectField', [], {'null': 'True'}),
            'rcn': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['cordis']