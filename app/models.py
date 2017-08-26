# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from distribution.db import TimestampedModel

# Create your models here.


class Ticket(TimestampedModel):
    ticket_id = models.CharField(max_length=30, unique=True)
    user = models.CharField(max_length=100)
    status = models.SmallIntegerField(default=1)

    def __unicode__(self):
        return self.ticket_id
