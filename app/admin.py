# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import *


admin.site.register(Sales)
admin.site.register(Custom)
admin.site.register(Engineer)
admin.site.register(TicketTemplate)
admin.site.register(Ticket)