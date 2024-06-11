from __future__ import annotations

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView

from .forms import ChooseClass


class ChooseClasses(LoginRequiredMixin, FormView):
    template_name = "choose-classes.html"
    form_class = ChooseClass

    course_choosen: int

    def get_form_kwargs(self):
        return super().get_form_kwargs() | {"user": self.request.user}

    def get_success_url(self):
        return reverse_lazy("grades", args=[self.course_choosen])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["account"] = self.request.user
        return context

    def form_valid(self, form):
        self.course_choosen = form.cleaned_data["class"]
        return super().form_valid(form)


# TODO: Replace with javascript on login page
class LoadingScreen(View):
    def get(self, request, *args, **kwargs):
        account = self.protected_login(
            self.request.user.username,
            self.request.session["sis-password"],
            self.request.session["domain"],
        )
        if isinstance(account, str):
            print(account)
            return HttpResponseRedirect(reverse("login-page"))
        return HttpResponseRedirect(reverse("choose-classes"))

    def protected_login(self, username: str, password: str, domain: str):
        from sisview.synergy import login

        try:
            return login(
                username=username,
                password=password,
                domain=domain,
                user=self.request.user,
            )
        except Exception as e:
            return str(e)
