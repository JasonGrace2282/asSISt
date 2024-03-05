from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import LoginForm


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('loading-screen')

    def form_valid(self, form: LoginForm):
        self.request.session['SIS_AUTH_USER_INFO'] = {
            'username': form.cleaned_data["username"],
            'password': form.cleaned_data["password"],
            'domain': (
                domain
                if (domain := form.cleaned_data["domain"])
                else "sisstudent.fcps.edu/SVUE"  # adding https:// breaks it
            )
        }
        return super().form_valid(form)
