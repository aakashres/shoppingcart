from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View, CreateView, UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import *
from django.contrib.auth.models import Group

from cart.models import Cart, Wishlist, Point, Order
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

class TestAdmin(TemplateView):
    template_name = "testadmin.html"


class TestFrontend(TemplateView):
    template_name = "testfront.html"


class RegistrationView(View):
    def get(self, request):
        userForm = UserForm()
        profileForm = ProfileForm()
        context = {
            'userForm': userForm,
            'profileForm': profileForm,
        }
        return render(request, 'account/registration.html', context)

    def post(self, request):
        userForm = UserForm(request.POST or None)
        profileForm = ProfileForm(request.POST or None)
        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save(commit=False)
            profile = profileForm.save(commit=False)
            password = userForm.cleaned_data.get('password2')
            user.set_password(password)
            user.save()
            profile.user = user
            profile.save()
            Cart.objects.create(user=user)
            Wishlist.objects.create(user=user)
            Point.objects.create(user=user)
            Order.objects.create(user=user)
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
        return render(request, 'account/registration.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'account/login.html', context)

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
        return render(request, 'account/login.html', context)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(request)
        messages.success(request, "Logged Out Successfully")
        return redirect('account:testadmin')


class ProfileDetailView(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs['slug']
        user = get_object_or_404(User, username=slug)
        userProfile = get_object_or_404(UserProfile, user=user)
        context = {
            'user': user,
            'userProfile': userProfile,
        }
        return render(request, 'account/profileDetail.html', context)


class ProfileUpdateView(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs['slug']
        user = get_object_or_404(User, username=slug)
        userProfile = get_object_or_404(UserProfile, user=user)
        userForm = UserUpdateForm(instance=user)
        profileForm = ProfileForm(instance=userProfile)
        print(userForm, profileForm)
        context = {
            'user': user,
            'userForm': userForm,
            'profileForm': profileForm,
        }
        return render(request, 'account/profileUpdate.html', context)

    def post(self, request, *args, **kwargs):
        slug = kwargs['slug']
        user = get_object_or_404(User, username=slug)
        userProfile = get_object_or_404(UserProfile, user=user)
        userForm = UserUpdateForm(request.POST or None, instance=user)
        profileForm = ProfileForm(request.POST or None, instance=userProfile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            return redirect('account:test')
        else:
            print(userForm.errors)
        context = {
            'user': user,
            'userForm': userForm,
            'profileForm': profileForm,
        }
        return render(request, 'account/profileUpdate.html', context)


class WishlistView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'account/wishlist.html', context)


class CartView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'account/cart.html', context)


class AddressAddView(SuccessMessageMixin, CreateView):
    model = Address
    template_name = 'account/addressAdd.html'
    form_class = AddressForm
    success_message = "Address Successfully Added"

    def dispatch(self, request, *args, **kwargs):
        username = kwargs['username']
        self.user = User.objects.get(username=username)
        return super(AddressAddView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form, **kwargs):
        billing_address = Address.objects.filter(billing_address=True)
        shipping_address = Address.objects.filter(shipping_address=True)
        if not billing_address:
            form.instance.billing_address = True
        if not shipping_address:
            form.instance.shipping_address = True
        form.instance.user = self.user
        form.save()
        return super(AddressAddView, self).form_valid(form, *kwargs)

    def get_success_url(self):
        return reverse("account:addressList",
                       kwargs={'username': self.user.username}
                       )


class AddressListView(ListView):
    model = Address
    template_name = 'account/addressList.html'
    context_object_name = 'addresses'

    def dispatch(self, request, *args, **kwargs):
        username = kwargs['username']
        self.user = User.objects.get(username=username)
        return super(AddressListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = kwargs
        context['user'] = self.user
        context['addresses'] = Address.objects.filter(
            user=self.user, deleted_at=None)
        return context

    def get_queryset(self):
        return Address.objects.filter(user=self.user, deleted_at=None)


class AddressUpdateView(SuccessMessageMixin, UpdateView):
    model = Address
    template_name = 'account/addressUpdate.html'
    form_class = AddressForm
    success_message = "Address Successfully Updated"

    def dispatch(self, request, *args, **kwargs):
        username = kwargs['username']
        self.user = User.objects.get(username=username)
        return super(AddressUpdateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form, **kwargs):
        form.instance.user = self.user
        form.save()
        return super(AddressUpdateView, self).form_valid(form, *kwargs)

    def get_success_url(self):
        return reverse("account:addressList",
                       kwargs={'username': self.user.username}
                       )
