from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class News(models.Model):
	'''
	//TO DO
	1. active selector form
	2. if want to add links in the body
	3. if need the begin and end date
	4. for 2, it would be better to save all links in one model
	'''
	body = models.CharField(max_length=140)
	pub_date = models.DateField('date published')
	active = models.IntegerField(default=1) # 1 means active while 0 means deactive

	# what will be shown in admin site
	def __str__(self):
		return self.body

	# set the plural form of News class
	class Meta:
		verbose_name_plural = 'news'

@python_2_unicode_compatible
class Members(models.Model):
	name = models.CharField(max_length=20)
	icon = models.ImageField(upload_to = 'members_icon/', default = 'members_icon/xxx/icon.png')

	def __str__(self):
		return self.name