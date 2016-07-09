from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import date
import os
def get_upload_path(instance, filename):
    return os.path.join(
      "member/static/member/", filename)

@python_2_unicode_compatible
class Member(models.Model):
	name = models.CharField(max_length=20)
	rank = models.IntegerField(default=0)
	icon = models.ImageField(upload_to = get_upload_path)
	title = models.CharField(max_length=140, blank=True, default='Default')
	intro_body = models.TextField(blank = True, default='Default')
	create_date = models.DateField(default=date.today)

	def __str__(self):
		return self.name