from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^testadmin/$', TestAdmin.as_view(), name="testadmin"),
    url(r'^testfront/$', TestFrontend.as_view(), name="test"),
    url(r'^register/$', FrontendRegistrationView.as_view(),
        name="frontendRegistration"),
    url(r'^login/$', FrontendLoginView.as_view(),
        name="frontendLogin"),
    url(r'^logout/$', FrontendLogoutView.as_view(),
        name="frontendLogout"),
]
