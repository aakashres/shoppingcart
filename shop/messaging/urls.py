from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^admin/$',
        AdminMessage.as_view(), name="adminMessage"),
    url(r'^admin/(?P<slug>[\w-]+)/$',
        AdminMessage.as_view(), name="adminMessage"),
]
