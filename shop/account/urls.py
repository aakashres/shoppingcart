from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^testadmin/$', TestAdmin.as_view(), name="testadmin"),
    url(r'^testfront/$', TestFrontend.as_view(), name="test"),
    url(r'^accounts/register/$', RegistrationView.as_view(),
        name="registration"),
    url(r'^accounts/login/$', LoginView.as_view(),
        name="login"),
    url(r'^accounts/logout/$', LogoutView.as_view(),
        name="logout"),


    url(r'^(?P<slug>[\w-]+)/$',
        ProfileDetailView.as_view(), name='profileDetail'),
    url(r'^(?P<slug>[\w-]+)/update/$',
        ProfileUpdateView.as_view(), name='profileUpdate'),

    url(r'^(?P<username>[\w-]+)/wishlist/$',
        WishlistView.as_view(), name='wishList'),
    url(r'^(?P<username>[\w-]+)/cart/$',
        CartView.as_view(), name='cart'),
    url(r'^(?P<username>[\w-]+)/address/add$',
        AddressAddView.as_view(), name='addressAdd'),
    url(r'^(?P<username>[\w-]+)/address/$',
        AddressListView.as_view(), name='addressList'),
    url(r'^(?P<username>[\w-]+)/address/(?P<pk>\d+)/update/$',
        AddressUpdateView.as_view(), name='addressUpdate'),


]
