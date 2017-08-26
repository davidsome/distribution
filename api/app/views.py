# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from app.models import Ticket


class TicketResource(DjangoResource):
    # Controls what data is included in the serialized output.
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'ticket_id': 'ticket_id',
        'status': 'status',
    })

    # GET /
    def list(self):
        return Ticket.objects.all()

    # GET /pk/
    def detail(self, pk):
        return Ticket.objects.get(id=pk)

    # POST /
    def create(self):
        return Ticket.objects.create(
            ticket_id=self.data['ticket_id'],
            user=self.data['user'],
            status=self.data['status']
        )

    # PUT /pk/
    def update(self, pk):
        try:
            post = Ticket.objects.get(id=pk)
        except Ticket.DoesNotExist:
            post = Ticket()

        post.title = self.data['title']
        post.user = Ticket.objects.get(username=self.data['author'])
        post.content = self.data['body']
        post.save()
        return post

    # DELETE /pk/
    def delete(self, pk):
        Ticket.objects.get(id=pk).delete()