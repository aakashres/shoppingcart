from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, UpdateView
from django.utils.text import slugify
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here


def getDateTime(datetime):
    date, time, meridiem = datetime.split(" ")
    hour, minute = time.split(":")
    if meridiem == "PM":
        hr = int(hour) + 12
        hr %= 24
        hour = str(hr)
    time = hour + ':' + minute
    datetime = date + ' ' + time
    return datetime


class AdminCouponCreateView(SuccessMessageMixin, CreateView):
    model = Coupon
    template_name = 'cart/adminCouponCreate.html'
    form_class = CouponForm
    success_url = reverse_lazy("message:adminMessage")
    success_message = "Coupon Successfully Added"

    def form_valid(self, form, **kwargs):
        couponObjects = Coupon.objects.filter(code=form.instance.code)
        if couponObjects:
            messages.error(self.request, "Coupon Code Already Exist!!!")
            return redirect('cart:adminCouponCreate')
        else:
            form.instance.valid_from = getDateTime(
                form.cleaned_data.get('validFrom'))
            form.instance.valid_to = getDateTime(
                form.cleaned_data.get('validTo'))
            form.save()

        return super(AdminCouponCreateView, self).form_valid(form, *kwargs)


class AdminCouponUpdateView(SuccessMessageMixin, UpdateView):
    model = Coupon
    template_name = 'cart/adminCouponUpdate.html'
    form_class = CouponForm
    success_url = reverse_lazy("message:adminMessage")
    success_message = "Coupon Successfully Updated"

    def form_valid(self, form, **kwargs):
        couponObjects = Coupon.objects.filter(code=form.instance.code)
        if couponObjects:
            messages.error(self.request, "Coupon Code Already Exist!!!")
            return redirect('cart:adminCouponCreate')
        else:
            form.instance.valid_from = getDateTime(
                form.cleaned_data.get('validFrom'))
            form.instance.valid_to = getDateTime(
                form.cleaned_data.get('validTo'))
            form.save()

        return super(AdminCouponCreateView, self).form_valid(form, *kwargs)


class AdminCouponListView(ListView):
    model = Coupon
    template_name = 'cart/adminCouponList.html'
    context_object_name = 'coupons'

    def get_queryset(self):
        return Coupon.objects.filter(deleted_at=None)


class AdminCategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'cart/adminCategoryCreate.html'
    form_class = CategoryForm
    success_url = reverse_lazy("message:adminMessage")
    success_message = "Category Successfully Added"

    def form_valid(self, form, **kwargs):
        categoryObjects = Category.objects.filter(slug=form.instance.title)
        if not categoryObjects:
            form.instance.slug = slugify(form.instance.title)
            form.save()
        else:
            messages.error(self.request, "Category Already Exist!!!")
            return redirect('cart:adminCategoryCreate')

        return super(AdminCategoryCreateView, self).form_valid(form, *kwargs)


class AdminCategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Category
    template_name = 'cart/adminCategoryUpdate.html'
    form_class = CategoryForm
    success_url = reverse_lazy("message:adminMessage")
    success_message = "Category Successfully Updated"

    def form_valid(self, form, **kwargs):
        categoryObjects = Category.objects.filter(slug=form.instance.title)
        if not categoryObjects:
            form.instance.slug = slugify(form.instance.title)
            form.save()
        else:
            messages.error(self.request, "Category Already Exist!!!")
            return redirect('cart:adminCategoryCreate')

        return super(AdminCategoryCreateView, self).form_valid(form, *kwargs)


class AdminCategoryListView(ListView):
    model = Category
    template_name = 'cart/adminCategoryList.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.filter(deleted_at=None)


class AdminProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    template_name = 'cart/adminProductCreate.html'
    form_class = ProductForm
    success_url = reverse_lazy("message:adminMessage")
    success_message = "Product Successfully Added"


class AdminSiteConfigCreateView(SuccessMessageMixin, CreateView):
    model = SiteConfig
    template_name = 'cart/adminSiteConfigCreate.html'
    form_class = SiteConfigForm
    success_url = reverse_lazy("message:adminMessage")
    success_message = "Site Config Successfully Added"


class AdminSiteConfigUpdateView(SuccessMessageMixin, UpdateView):
    model = SiteConfig
    template_name = 'cart/adminSiteConfigUpdate.html'
    form_class = SiteConfigForm
    success_url = reverse_lazy("message:adminMessage")
    success_message = "Site Config Successfully Updated"


class AdminSiteConfigListView(ListView):
    model = SiteConfig
    template_name = 'cart/adminSiteConfigList.html'
    context_object_name = 'siteConfigs'

    def get_queryset(self):
        return SiteConfig.objects.filter(deleted_at=None)
