from __future__ import annotations

from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    domain = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control mb-3 element"}),
        initial="sisstudent.fcps.edu/SVUE",
    )

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"placeholder": "Username", "class": "form-control element"}
        )
        self.fields["password"].widget.attrs.update(
            {"placeholder": "Password", "class": "form-control element"}
        )

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                self.user_cache = self.create_user()
            self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        self.request.session["domain"] = self.cleaned_data["domain"]
        self.request.session["sis-password"] = self.cleaned_data["password"]
        return super().confirm_login_allowed(user)

    def create_user(self):
        user, _created = get_user_model().objects.get_or_create(
            username=self.cleaned_data["username"]
        )
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user
