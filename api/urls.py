from django.conf.urls import url, include


from app.views import TicketResource

urlpatterns = [
    # The usual fare, then...

    # Add this!
    url(r'tickets/', include(TicketResource.urls())),
]