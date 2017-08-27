#  -*- coding: utf-8 -*-
from django.conf.urls import url, include

from app.views import *


urlpatterns = [
    # The usual fare, then...

    # Add this!
    url(r'sales/', include(SalesResource.urls())),
    url(r'customs/', include(CustomResource.urls())),
    url(r'engineers/', include(EngineerResource.urls())),
    url(r'products/', include(ProductsResource.urls())),
    url(r'areas/', include(AreaResource.urls())),
    url(r'templates/', include(TicketTemplateResource.urls())),
    url(r'tickets/', tickets),
    url(r'templates2/', templates2),
]