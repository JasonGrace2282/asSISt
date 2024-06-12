from __future__ import annotations

from django import forms, http


class ChooseClass(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        classes = [(subject.id, subject.name) for subject in user.subjects.all()]
        self.fields["class"] = forms.ChoiceField(
            choices=classes,
            widget=forms.RadioSelect(attrs={"class": "class-radio"}),
        )

        if not classes:
            raise http.Http404
