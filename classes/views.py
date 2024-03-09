from django.shortcuts import HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.views import View
from django.urls import reverse
from django.contrib import messages
from sisview.models import Account
from .models import ClassButton


class ChooseClasses(ListView):
    model = ClassButton
    template_name = "choose-classes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = Account.objects.get(  # type: ignore
            pk=self.request.session.get("SIS_AUTH_USER_INFO")
        )
        context['username'] = str(account.name)
        context['classes'] = [
            subject.name
            for subject in account.subjects.all()
        ]
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get("course") is None:
            return self.get(request, *args, **kwargs)
        self.request.session['SUBJECT'] = request.POST.get('course')
        return HttpResponseRedirect('grades')


class LoadingScreen(View):
    def get(self, request, *args, **kwargs):
        info = request.session.get("SIS_AUTH_USER_INFO")
        account = self.protected_login(**info)
        if isinstance(account, str):
            return HttpResponseRedirect(reverse('login-page'))
        request.session["SIS_AUTH_USER_INFO"] = account.id
        return HttpResponseRedirect(reverse('choose-classes'))

    @staticmethod
    def protected_login(
        username: str,
        password: str,
        domain: str
    ) -> Account | str:
        from sisview.synergy import login
        try:
            return login(
               username=username,
               password=password,
               domain=domain
            )
        except Exception as e:
            return str(e)
