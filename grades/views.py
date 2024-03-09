from django.views.generic import FormView
from django.urls import reverse_lazy
from sisview.models import Account
from .forms import get_grades_form


class CalcGrades(FormView):
    template_name = "grades.html"
    success_url = reverse_lazy('choose-classes')

    fg = None
    '''Final Grade override'''

    @property
    def form_class(self):
        """The form_class created."""
        account = Account.objects.get(  # type: ignore
            id=self.request.session.get("SIS_AUTH_USER_INFO")
        )
        subject_name = self.request.session.get('SUBJECT')

        weights = []
        for subject in account.subjects.all():
            if str(subject.name).upper() == subject_name.upper():
                weights += [x.name for x in subject.weights.all()]

        return get_grades_form(weights, len(weights))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = Account.objects.get(  # type: ignore
            id=self.request.session.get("SIS_AUTH_USER_INFO")
        )
        subject_name = self.request.session.get('SUBJECT')
        for subject in account.subjects.all():
            if str(subject.name).upper() == subject_name.upper():
                weights = subject.weights.all()
                context['weights'] = [x.name for x in weights]
                context['statuses'] = [
                    x.get_status()
                    for x in weights
                ]
                context['classname'] = subject_name
                context['rows'] = range(3)
                context['fg'] = (
                    self.fg
                    if self.fg is not None
                    else subject.get_final_grade({})
                )
        return context

    def form_valid(self, form):
        def pcall(f, *args, **kwargs):
            try:
                return f(*args, **kwargs)
            except ValueError:
                return None

        sims = {}
        account = Account.objects.get(  # type: ignore
            id=self.request.session.get("SIS_AUTH_USER_INFO")
        )
        subject_name = self.request.session.get('SUBJECT')
        for subject in account.subjects.all():
            if str(subject.name).upper() == subject_name.upper():
                break
        else:
            return  # uh oh no matches?

        for weight in subject.weights.all():
            sims[weight.name] = []
            for row in range(3):
                tmp = pcall(
                    lambda x: [float(i) for i in x],
                    form.cleaned_data[f'{weight.name}_{row}'].replace(
                        " ", ""
                    ).split("/")
                )
                if tmp is None or len(tmp) != 2:
                    continue
                sims[weight.name].append(tmp)

        self.fg = subject.get_final_grade(category_sims=sims)
        return self.render_to_response(self.get_context_data())