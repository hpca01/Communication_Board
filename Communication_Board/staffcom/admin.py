# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from staffcom.models import Comm_Item, comment

# Register your models here.

admin.site.register(Comm_Item)
admin.site.register(comment)


