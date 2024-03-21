from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import LoginForm


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('loading-screen')

    def form_valid(self, form: LoginForm):
        form.cleaned_data["domain"] = (
                domain
                if (domain := form.cleaned_data["domain"])
                else "sisstudent.fcps.edu/SVUE"  # adding https:// breaks it
                # for LCPS it is
                # 'https://sis.lcps.org/PXP2_Login_Student.aspx'
                # TODO: Create buttons for other common ones like LCPS
            )
        for k, v in form.cleaned_data.items():
            self.request.session[k] = v
        return super().form_valid(form)
