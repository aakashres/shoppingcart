from django import forms
from .models import UserProfile, Address
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'required': 'true',
        'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'required': 'true',
        'placeholder': 'Password Confirm'}))

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields["first_name"].widget.attrs.update(
            {'placeholder': 'First Name', 'required': 'true'})
        self.fields["last_name"].widget.attrs.update(
            {'placeholder': 'Last Name', 'required': 'true'})
        self.fields["username"].widget.attrs.update(
            {'placeholder': 'Username', 'required': 'true'})
        self.fields["email"].widget.attrs.update(
            {'placeholder': 'E-Mail', 'required': 'true'})

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")

        return password2


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

        self.fields["first_name"].widget.attrs.update(
            {'placeholder': 'First Name'})
        self.fields["last_name"].widget.attrs.update(
            {'placeholder': 'Last Name', 'required': 'true'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "gender",
            "birthdate"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['birthdate'].widget.attrs.update(
            {'data-date-format': "YYYY-MM-DD",
             'placeholder': 'Birthdate',
             'required': 'true'})


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "address_line1",
            "address_line2",
            "contact_line1",
            "contact_line2",
            "landmark",
            "city",
            "district",
            "billing_address",
            "shipping_address",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if not field == "billing_address" and not field == "shipping_address":
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control'})
        self.fields["address_line1"].widget.attrs.update(
            {'placeholder': 'Address Line 1'})
        self.fields["address_line2"].widget.attrs.update(
            {'placeholder': 'Address Line 2'})
        self.fields["contact_line1"].widget.attrs.update(
            {'placeholder': 'Contact Line 1'})
        self.fields["contact_line2"].widget.attrs.update(
            {'placeholder': 'Contact Line 2'})
        self.fields["landmark"].widget.attrs.update(
            {'placeholder': 'Nearest Landmark'})
        self.fields["city"].widget.attrs.update(
            {'placeholder': 'City'})



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'required': 'true',
        'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'required': 'true',
        'placeholder': 'Password', }))

    class Meta:
        fields = [
            "username",
            "password",
        ]


class StaffForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class EmailForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'required': 'true',
            'id': 'email',
        }))
