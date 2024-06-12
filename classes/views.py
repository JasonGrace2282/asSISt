from __future__ import annotations

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

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


class LoadingScreen(LoginRequiredMixin, TemplateView):
    template_name =  "loading.html"


    def post(self, *args, **kwargs):
        account = self.protected_login(
            self.request.user.username,
            self.request.session.pop("sis-password"),
            self.request.session.pop("domain"),
        )
        error = account if isinstance(account, str) else ""
        return JsonResponse({"error": error})

    def protected_login(self, username: str, password: str, domain: str):
        from sisview.synergy import login

        try:
            login(
                username=username,
                password=password,
                domain=domain,
                user=self.request.user,
            )
        except KeyError:
            return "An internal error occurred, contact the maintainers for help!"
        except Exception as e:
            return str(e)
