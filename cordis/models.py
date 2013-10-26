from django.db import models
from picklefield.fields import PickledObjectField

import logging

# Create your models here.

class Project(models.Model):
	rcn = models.IntegerField(primary_key=True)
	# project_acronym = models.CharField(null=True,max_length=255)

	# This contains all the data parsed from Cordis
	data = PickledObjectField(null=True)

	def parse_cordis(self):
		from parse_cordis import project_xml
		self.data = project_xml.parse(self.rcn)
		# self.project_acronym = self.data
		print "Stored " + str(self.rcn)

	def __unicode__(self):
		return str(self.rcn)


class ProjectList(object):
	def __init__(self, data):
		self.data = data