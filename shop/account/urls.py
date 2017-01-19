from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^testadmin/$', TestAdmin.as_view()),
    url(r'^testfront/$', TestFrontend.as_view()),
]
