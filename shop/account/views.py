from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class TestAdmin(TemplateView):
    template_name = "testadmin.html"


class TestFrontend(TemplateView):
    template_name = "testfront.html"
