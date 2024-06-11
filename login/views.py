from __future__ import annotations

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import LoginForm


class AssistLoginView(LoginView):
    template_name = "login.html"
    authentication_form = LoginForm
    next_page = reverse_lazy("loading")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["errors"] = self.request.GET.get("error", "")
        return ctx
