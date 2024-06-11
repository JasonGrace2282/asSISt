from __future__ import annotations

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import GradesForm


class CalcGrades(FormView):
    template_name = "grades.html"
    success_url = reverse_lazy("choose-classes")
    form_class = GradesForm

    fg = None
    """Final Grade override"""

    def get_form_kwargs(self, *args, **kwargs):
        """The form_class created."""
        kw = super().get_form_kwargs(*args, **kwargs)

        subject = get_object_or_404(self.request.user.subjects, pk=self.kwargs["course_id"])
        weights = [x.name for x in subject.weights.all()]

        kw["weights"] = weights
        return kw

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject_id = self.kwargs["course_id"]
        subject = get_object_or_404(self.request.user.subjects, pk=subject_id)
        weights = subject.weights.all()

        context["course"] = subject_id
        context["weights"] = [x.name for x in weights]
        context["statuses"] = [x.get_status() for x in weights]
        context["classname"] = subject.name
        context["rows"] = range(3)
        context["fg"] = self.fg if self.fg is not None else subject.get_final_grade({})
        return context

    def form_valid(self, form):  # type: ignore
        def pcall(f, *args, **kwargs):
            try:
                return f(*args, **kwargs)
            except ValueError:
                return None

        sims = {}
        subject_id = self.kwargs["course_id"]
        subject = get_object_or_404(self.request.user.subjects, pk=subject_id)

        for weight in subject.weights.all():
            sims[weight.name] = []
            for row in range(3):
                tmp = pcall(
                    lambda x: [float(i) for i in x],
                    form.cleaned_data[f"{weight.name}_{row}"].replace(" ", "").split("/"),
                )
                if tmp is None or len(tmp) != 2:
                    continue
                sims[weight.name].append(tmp)

        self.fg = subject.get_final_grade(category_sims=sims)
        return self.render_to_response(self.get_context_data())
