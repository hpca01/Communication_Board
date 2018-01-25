# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from staffcom.models import Comm_Item, comment

admin.site.site_header = "Communication Board"
# Register your models here.

#admin.site.register(Comm_Item)
#admin.site.register(comment) -- freedom of press, people should be able to write whatever comments they want.

@admin.register(Comm_Item)
class Comm_ItemAdmin(admin.ModelAdmin):
	date_hierarchy = 'date'
	list_display = ('comm_type', 'created_by', 'visible', 'date')


