from django import forms
from .models import *


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = [
            "title",
            "code",
            "valid_from",
            "valid_to",
            "validity_count",
            "discount_type",
            "discount_percent",
            "discount_amount",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control'})
        self.fields['discount_type'].widget.attrs.update({'id': 'select-list'})
        self.fields['valid_from'].widget.attrs.update(
            {'class': 'datetimepicker form-control'})
        self.fields['valid_to'].widget.attrs.update(
            {'class': 'datetimepicker form-control'})


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "title",
            "parent",
            "description",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control'})
        self.fields['parent'].widget.attrs.update({'id': 'select-list'})
        self.fields['description'].widget.attrs.update({'id': 'summernote'})


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "reference_code",
            "barcode",
            "visibility",
            "photos",
            "description",
            "quantity",
            "categories",
            "tags",
            "price",
            "vat",
            "vat_included",
            "discount_percent",
            "discount_amount",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'id': 'summernote'})
        self.fields['categories'].widget.attrs.update({'id': 'select-list'})
        self.fields['tags'].widget.attrs.update({'data-role': 'tagsinput'})


class SiteConfigForm(forms.ModelForm):
    class Meta:
        model = SiteConfig
        fields = [
            "key",
            "value",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control'})
