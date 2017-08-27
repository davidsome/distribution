# encoding: utf-8
from django.conf.urls import url, include
from app.views import *


urlpatterns = [
    # The usual fare, then...

    # Add this!
    url(r'^$', index),
    url(r'^createTicket', create_ticket),
    url(r'^ticketDetail', ticket_detail),
    url(r'^logout', logout),
    url(r'^login', login),
]