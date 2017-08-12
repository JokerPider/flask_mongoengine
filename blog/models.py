# coding: utf-8
import datetime
from flask import url_for
from blog import db

class Post(db.Document):

	create_time = db.DateTimeField(default=datetime.datetime.now, required=True)
	title = db.StringField(max_length=255, required=True)
	slug = db.StringField(max_length=255, required=True)
	body = db.StringField(max_length=255, required=True)
	comments = db.ListField(db.EmbeddedDocumentField('Comment'))

	def get_absolute_url(self):
		return url_for('post', kwargs={'slug': self.slug})

	def __unicode__(self):
		return self.title

	mate = {
		'allow_inheritance': True,
		'indexes': ['-create_time', 'slug'],
		'ordering': ['-create_time']
	}


class Comment(db.EmbeddedDocument):
	create_time = db.DateTimeField(default=datetime.datetime.now, required=True)
	body = db.StringField(verbose_name='Comnent', required=True)
	author = db.StringField(verbose_name='Name', max_length=255)
