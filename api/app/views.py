# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from collections import OrderedDict

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
    'products': {
        'db': Products,
        'fields': {
            'id': 'id',
            'name': 'name',
            'remark': 'remark'
        }
    },
    'areas': {
        'db': Area,
        'fields': {
            'id': 'id',
            'name': 'name',
            'remark': 'remark'
        }
    },
}


class ProductsResource(DjangoResource):

    preparer = FieldsPreparer(fields=DBMapping['products']['fields'])

    def list(self, *args, **kwargs):
        return DBMapping['products']['db'].objects.all()


class AreaResource(DjangoResource):
    preparer = FieldsPreparer(fields=DBMapping['areas']['fields'])

    def list(self, *args, **kwargs):
        return DBMapping['areas']['db'].objects.all()


class SalesResource(DjangoResource):
    """ 展示销售数据
    """
    preparer = FieldsPreparer(fields=DBMapping['sales']['fields'])

    def list(self):
        return DBMapping['sales']['db'].objects.all()

    # GET /pk/
    def detail(self, pk):
        return DBMapping['sales']['db'].objects.get(id=pk)


class CustomResource(DjangoResource):
    """ 展示客户数据
    """
    preparer = FieldsPreparer(fields=DBMapping['customs']['fields'])

    def list(self):
        return DBMapping['customs']['db'].objects.all()

    # GET /pk/
    def detail(self, pk):
        return DBMapping['customs']['db'].objects.get(id=pk)


class EngineerResource(DjangoResource):
    """ 展示工程师数据
    """
    preparer = FieldsPreparer(fields=DBMapping['engineers']['fields'])

    def list(self):
        return DBMapping['engineers']['db'].objects.all()

    # GET /pk/
    def detail(self, pk):
        return DBMapping['engineers']['db'].objects.get(id=pk)


class TicketTemplateResource(DjangoResource):
    """ 工单模板数据
    """
    preparer = FieldsPreparer(fields=DBMapping['templates']['fields'])

    def list(self, *args, **kwargs):
        print args, kwargs
        print self.data
        return DBMapping['templates']['db'].objects.all()

    # GET /pk/
    def detail(self, pk):
        return DBMapping['templates']['db'].objects.get(id=pk)


def common_response(status=True, message="success", data=list()):
    return JsonResponse({
        "status": status,
        "message": message,
        "data": data
    })


def templates2(request):
    data = []
    for d in TicketTemplate.objects.values("type_1").distinct():
        type_1_sub = []
        for d2 in TicketTemplate.objects.filter(type_1=d["type_1"]).values("type_2").distinct():
            type_3_sub = []
            for d3 in TicketTemplate.objects.filter(type_2=d2["type_2"],
                                                    type_1=d["type_1"]).values("type_3").distinct():
                type_4_sub = []
                for d4 in TicketTemplate.objects.filter(type_3=d3["type_3"],
                                                        type_2=d2["type_2"],
                                                        type_1=d["type_1"])\
                        .values("type_4").distinct():
                    type_4_sub.append({
                        "name": d4["type_4"],
                        "value": TicketTemplate.objects.get(type_4=d4["type_4"]).id
                    })
                type_3_sub.append({
                    "name": d3["type_3"],
                    "value": 0,
                    "sub": type_4_sub
                })
            type_1_sub.append({
                "name": d2["type_2"],
                "value": 0,
                "sub": type_3_sub
            })
        data.append({
            "name": d["type_1"],
            "value": 0,
            "sub": type_1_sub
        })
    print data
    return common_response(data=data)


def generate_ticket_id():
    import uuid
    return str(uuid.uuid1())[0:10]


@csrf_exempt
def tickets(request):
    if request.method == "GET":
        data = []
        # detail
        if request.GET.get("ticket_id"):
            t = Ticket.objects.get(ticket_id=request.GET.get("ticket_id"))
            d = OrderedDict()
            d["ticket_id"] = t.ticket_id
            d["pro_name"] = t.pro_name
            d["engineer"] = t.engineer.name
            d["product"] = t.product.name
            d["sale"] = t.sale.name
            d["customer"] = t.custom.name
            d["status"] = t.get_status_display()
            d["trouble_report"] = t.trouble_report
            d["knowledge_report"] = t.knowledge_report
            d["service_start"] = t.service_start
            d["service_end"] = t.service_end
            d["score"] = t.score
            d["remark"] = t.remark
            return common_response(data=d)
        # all
        else:
            for t in Ticket.objects.all():
                d = OrderedDict()
                d["ticket_id"] = t.ticket_id
                d["pro_name"] = t.pro_name
                d["engineer"] = t.engineer.name
                d["product"] = t.product.name
                d["sale"] = t.sale.name
                d["customer"] = t.custom.name
                d["status"] = t.get_status_display()
                data.append(d)
            if request.GET.get("render") == "dataTables":
                new_data = []
                for d in data:
                    new_data.append(d.values())
                return JsonResponse({"data": new_data})
            else:
                return common_response(data=data)
    elif request.method == "POST":
        # create ticket
        Ticket.objects.create(
            ticket_id=generate_ticket_id(),
            pro_name=request.POST.get("pro_name"),
            engineer_id=request.POST.get("engineer"),
            sale_id=request.POST.get("sale"),
            custom_id=request.POST.get("customer"),
            ticket_temp_id=request.POST.get("ticket_temp"),
            product_id=request.POST.get("product"),
            area_id=request.POST.get("area"),
            service_start=request.POST.get("service_start"),
            service_end=request.POST.get("service_end")
        )
        return common_response()

