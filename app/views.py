# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    # return render_to_response("app/index.html")
    return render(request, "app/index.html")


def create_ticket(request):
    # return render_to_response("app/create_ticket.html")
    return render(request, "app/create_ticket.html")


def ticket_detail(request):
    # return render_to_response("app/create_ticket.html")
    return render(request, "app/ticket_detail.html")


def login(request):
    return HttpResponseRedirect('/admin')


def logout(request):
    return HttpResponseRedirect('/admin')

