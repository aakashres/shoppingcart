from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^shopAdmin/category/create/$',
        AdminCategoryCreateView.as_view(), name="adminCategoryCreate"),
    url(r'^shopAdmin/category/(?P<pk>\d+)/update/$',
        AdminCategoryUpdateView.as_view(), name="adminCategoryUpdate"),
    url(r'^shopAdmin/category/list/$',
        AdminCategoryListView.as_view(), name="adminCategoryList"),


    url(r'^shopAdmin/coupon/create/$',
        AdminCouponCreateView.as_view(), name="adminCouponCreate"),
    url(r'^shopAdmin/coupon/list/$',
        AdminCouponListView.as_view(), name="adminCouponList"),
    url(r'^shopAdmin/coupon/(?P<pk>\d+)/update/$',
        AdminCouponUpdateView.as_view(), name='adminCouponUpdate'),
    url(r'^shopAdmin/coupon/(?P<pk>\d+)/update/$',
        AdminCouponUpdateView.as_view(), name='adminCouponUpdate'),

    url(r'^shopAdmin/product/create/$',
        AdminProductCreateView.as_view(), name="adminProductCreate"),

    url(r'^shopAdmin/siteconfig/create/$',
        AdminSiteConfigCreateView.as_view(), name="adminSiteConfigCreate"),
    url(r'^shopAdmin/siteconfig/list/$',
        AdminSiteConfigListView.as_view(), name="adminSiteConfigList"),
    url(r'^shopAdmin/siteconfig/(?P<pk>\d+)/update/$',
        AdminSiteConfigUpdateView.as_view(), name="adminSiteConfigUpdate"),
]
