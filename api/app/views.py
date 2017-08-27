# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
    print request.method
    if request.method == "GET":
        data = []
        for t in Ticket.objects.all():
            data.append({
                "ticket_id": t.ticket_id,
                "pro_name": t.pro_name,
                "engineer": t.engineer.name,
                "product": t.product.name,
                "sale": t.sale.name,
                "customer": t.custom.name,
                "status": t.get_status_display(),
            })
        if request.GET.get("render") == "dataTables":
            new_data = []
            for d in data:
                new_data.append(d.values())
            return JsonResponse({"data": new_data})
        else:
            return common_response(data=data)
    elif request.method == "POST":
        print request.POST.get("service_start")
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

