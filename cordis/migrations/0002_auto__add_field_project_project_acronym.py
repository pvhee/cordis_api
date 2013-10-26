# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.project_acronym'
        db.add_column(u'cordis_project', 'project_acronym',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.project_acronym'
        db.delete_column(u'cordis_project', 'project_acronym')


    models = {
        u'cordis.project': {
            'Meta': {'object_name': 'Project'},
            'data': ('picklefield.fields.PickledObjectField', [], {'null': 'True'}),
            'project_acronym': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'rcn': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['cordis']