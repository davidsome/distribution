# encoding: utf-8
from django.conf.urls import url, include
from app.views import *


urlpatterns = [
    # The usual fare, then...

    # Add this!
    url(r'^$', index),
    url(r'^createTicket.html', create_ticket),
    url(r'^ticketDetail.html', ticket_detail),
    url(r'^logout.html', logout),
    url(r'^login.html', login),
]