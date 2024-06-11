from __future__ import annotations

from django import forms
from django.utils.safestring import SafeString


class GradesForm(forms.Form):
    def __init__(self, weights: list[str], *args, **kwargs):
        super().__init__(*args, **kwargs)
        for weight in weights:
            for i in range(3):  # todo: make this configurable
                self.fields[f"{weight}_{i}"] = forms.CharField(
                    required=False,
                    widget=forms.TextInput(
                        attrs={
                            "placeholder": "points / total",
                            "class": "form-control grade-element",
                        }
                    ),
                )

        self.columns = len(weights)

    def as_table(self) -> SafeString:
        table = str(super().as_table())
        table_list = table.split("\n")
        final = ""
        tr_count = 0
        for chunk in table_list:
            chunk = chunk.strip()
            if "<label" in chunk:
                continue
            elif "</tr>" in chunk:
                tr_count += 1
            if tr_count % self.columns != 0 and chunk in {"<tr>", "</tr>"}:
                continue
            final += chunk + "\n"
        return SafeString(final)
