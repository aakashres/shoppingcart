from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import *
from django.contrib.auth.models import Group


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
        userForm = UserForm(request.POST or None)
        profileForm = ProfileForm(request.POST or None)
        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save(commit=False)
            profile = profileForm.save(commit=False)
            password = user.password
            user.set_password(password)
            user.save()
            profile.user = user
            profile.save()
            grp = Group.objects.get(name='Customer')
            grp.user_set.add(user)

            user = authenticate(username=user.username, password=password)
            messages.success(request, "Registration Successful")
            login(request, user)
            return redirect('account:test')

        context = {
            'userForm': userForm,
            'profileForm': profileForm,
        }
        return render(request, 'account/frontendRegistration.html', context)


class FrontendLoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'account/frontendLogin.html', context)

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(username=username, password=password)
            print(type(user))
            if user:
                messages.success(request, "Logged In Successfully")
                login(request, user)
                return redirect('account:test')
            else:
                print("lool")
        else:
            print(form)
        messages.warning(request, "Log In Failure")
        context = {
            'form': form,
        }
        return render(request, 'account/frontendLogin.html', context)


class FrontendLogoutView(View):

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(request)
        messages.success(request, "Logged Out Successfully")
        return redirect('account:testadmin')
