# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from app.models import *



DBMapping = {
    'sales': {
        'db': Sales,
        'fields': {
            'id': 'id',
            'name': 'name',
            'address': 'address',
            'email': 'email',
            'phone': 'phone',
            'remark': 'remark'
        }
    },
    'customs': {
        'db': Custom,
        'fields': {
            'id': 'id',
            'name': 'name',
            'address': 'address',
            'email': 'email',
            'phone': 'phone',
            'remark': 'remark'
        }
    },
    'engineers': {
        'db': Engineer,
        'fields': {
            'id': 'id',
            'name': 'name',
            'gender': 'gender',
            'email': 'email',
            'phone': 'phone',
            'rank': 'rank',
            'remark': 'remark'
        }
    },
    'templates': {
        'db': TicketTemplate,
        'fields': {
            'id': 'id',
            'type_1': 'type_1',
            'type_2': 'type_2',
            'type_3': 'type_3',
            'type_4': 'type_4',
            'score': 'score',
            'level': 'level'
        }
    },
}



class SalesResource(DjangoResource):
    """ 展示销售数据
    """
    preparer = FieldsPreparer(fields=DBMapping['sales']['fields'])
    # 
    def list(self):
        return DBMapping['sales']['db'].objects.all()

    # GET /pk/
    def detail(self, pk):
        return DBMapping['sales']['db'].objects.get(id=pk)



class CustomResource(DjangoResource):
    """ 展示客户数据
    """
    preparer = FieldsPreparer(fields=DBMapping['customs']['fields'])
    # 
    def list(self):
        return DBMapping['customs']['db'].objects.all()

    # GET /pk/
    def detail(self, pk):
        return DBMapping['customs']['db'].objects.get(id=pk)



class EngineerResource(DjangoResource):
    """ 展示工程师数据
    """
    preparer = FieldsPreparer(fields=DBMapping['engineers']['fields'])
    # 
    def list(self):
        return DBMapping['engineers']['db'].objects.all()

    # GET /pk/
    def detail(self, pk):
        return DBMapping['engineers']['db'].objects.get(id=pk)



class TicketTemplateResource(DjangoResource):
    """ 工单模板数据
    """
    preparer = FieldsPreparer(fields=DBMapping['templates']['fields'])
    # 
    def list(self):
        return DBMapping['templates']['db'].objects.all()

    # GET /pk/
    def detail(self, pk):
        return DBMapping['templates']['db'].objects.get(id=pk)

