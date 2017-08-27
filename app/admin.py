# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import *


class BaseAdmin(admin.ModelAdmin):
    """ 后台信息基类
    """
    ordering = ('-created_at', )


class SalesAdmin(BaseAdmin):
    """ 销售信息后台
    """
    list_display = (
        'name', 'email', 'phone', 'remark'
        )
    search_fields = [
        'name', 'email', 'phone', 'remark'
        ]

admin.site.register(Sales, SalesAdmin)


class CunstomAdmin(BaseAdmin):
    """ 客户信息后台
    """
    list_display = (
        'name', 'email', 'phone', 'remark'
        )
    search_fields = [
        'name', 'email', 'phone', 'remark'
        ]

admin.site.register(Custom, CunstomAdmin)


class TicketInline(admin.StackedInline):
    model = Ticket
    extra = 1


class EngineerAdmin(BaseAdmin):
    """ 工程师信息后台
    """
    list_display = (
        'name', 'email', 'phone', 'rank', 'gender', 'cum_score', 'cur_score', 'remark'
        )
    inlines = [TicketInline, ]
    search_fields = [
        'name', 'email', 'phone', 'gender'
        ]

admin.site.register(Engineer, EngineerAdmin)


class TicketTemplateAdmin(BaseAdmin):
    """ 工单模板信息后台
    """
    list_display = (
        'type_1', 'type_2', 'type_3', 'type_4', 'score', 'level', 'remark'
        )
    inlines = [TicketInline, ]
    search_fields = [
        'type_1', 'type_2', 'type_3', 'type_4'
        ]

admin.site.register(TicketTemplate, TicketTemplateAdmin)


class TicketAdmin(BaseAdmin):
    """ 工单信息后台
    """
    list_display = (
        'ticket_id', 'pro_name', 'status', 'score', 'remark'
        )
    
    search_fields = [
        'ticket_id', 'pro_name', 'status'
        ]

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Products)
admin.site.register(Area)
