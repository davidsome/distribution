from django.conf.urls import url, include
from app.views import index


urlpatterns = [
    # The usual fare, then...

    # Add this!
    url(r'^', index),
]