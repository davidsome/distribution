from django.conf.urls import url, include
from app.views import *


urlpatterns = [
    # The usual fare, then...

    # Add this!
    url(r'^$', index),
    url(r'^createTicket', create_ticket)
]