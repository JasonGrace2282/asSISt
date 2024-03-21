from django.shortcuts import HttpResponseRedirect
from django.views.generic import FormView
from django.views import View
from django.urls import reverse
from sisview.models import Account
from .forms import ChooseClass


class ChooseClasses(FormView):
    template_name = "choose-classes.html"
    success_url = "grades"

    def get_form_class(self):
        form_class = ChooseClass
        form_class.account = Account.objects.get(
            pk=self.request.session["account_id"]
        )
        return form_class

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        account_id = self.request.session["account_id"]
        account = Account.objects.get(pk=account_id)
        context['username'] = str(account.name)
        return context

    def form_valid(self, form):
        self.request.session['SUBJECT'] = form.cleaned_data['class']
        return super().form_valid(form)


class LoadingScreen(View):
    def get(self, request, *args, **kwargs):
        account = self.protected_login(*[
            request.session[x]
            for x in ["username", "password", "domain"]
        ])
        if isinstance(account, str):
            print(account)
            return HttpResponseRedirect(reverse('login-page'))
        request.session["account_id"] = account.pk
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
