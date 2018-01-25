# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Comm_Item(models.Model):
	comm_types = [('Inventory','Inventory'),('Chemo','Chemo'),('Operation', 'Operation'), ('HomeIV','HOMEIV'),]
	title = models.CharField(max_length = 200, unique = True, help_text = "<br/>This could be drug name, or shift name, refer to guidelines of use.")
	comm_type = models.CharField(max_length=10, choices=comm_types, default = 'OPS')
	descr = HTMLField()
	date = models.DateField(auto_now=True)
	visible = models.BooleanField(default=True)
	created_by = models.ForeignKey(User, default = "", null=True, blank=True)

	def __str__(self):
		return self.title

	def typeofcomm(self):
		return self.comm_type

	def summary(self):
		return self.descr[:50]

	def get_comments(self):
		return self.comments.all().order_by('-date_time').values()

class comment(models.Model):
	content = HTMLField()
	date_time = models.DateField(auto_now=True)
	link_to_comm = models.ForeignKey('staffcom.Comm_Item', 
		related_name = "comments" ,on_delete = models.CASCADE)
	username = models.ForeignKey(User, default = "")

	def __str__(self):
		return str(self.content)