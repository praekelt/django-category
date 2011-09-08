# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('category_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('category', ['Category'])

        # Adding model 'Tag'
        db.create_table('category_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('category', ['Tag'])

        # Adding M2M table for field categories on 'Tag'
        db.create_table('category_tag_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm['category.tag'], null=False)),
            ('category', models.ForeignKey(orm['category.category'], null=False))
        ))
        db.create_unique('category_tag_categories', ['tag_id', 'category_id'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('category_category')

        # Deleting model 'Tag'
        db.delete_table('category_tag')

        # Removing M2M table for field categories on 'Tag'
        db.delete_table('category_tag_categories')


    models = {
        'category.category': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'category.tag': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Tag'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['category.Category']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['category']
