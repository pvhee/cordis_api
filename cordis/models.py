from django.db import models
from picklefield.fields import PickledObjectField

# Create your models here.

class Project(models.Model):
	rcn = models.IntegerField(primary_key=True)
	# project_acronym = models.CharField(null=True,max_length=255)

	# This contains all the data parsed from Cordis
	data = PickledObjectField(null=True)

	def parse_cordis(self):
		from parse_cordis import project
		self.data = project.parse(self.rcn)
		# self.project_acronym = self.data
		print "Parsed cordis and into model"

	def __unicode__(self):
		return str(self.rcn)


# class Listing(object):
# 	def __init__(self, data):
# 		self.data = data