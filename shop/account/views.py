from django.shortcuts import render
from django.views.generic import TemplateView, View
from .forms import *


# Create your views here.

class TestAdmin(TemplateView):
    template_name = "testadmin.html"


class TestFrontend(TemplateView):
    template_name = "testfront.html"


class FrontendRegistrationView(View):
    def get(self, request):
        userForm = UserForm()
        profileForm = ProfileForm()
        context = {
            'userForm': userForm,
            'profileForm': profileForm,
        }
        return render(request, 'account/frontendRegistration.html', context)

    def post(self, request):
        context = {
        }
        return render(request, 'account/frontendRegistration.html', context)
