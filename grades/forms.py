from django import forms
from django.utils.safestring import SafeString


    
def _as_table(self: forms.Form) -> str:
    table: str = super(type(self), self).as_table()
    table = table.split("\n")
    final = ""
    tr_count = 0
    for chunk in table:
        chunk = chunk.strip()
        if "<label" in chunk:
            continue
        elif "</tr>" in chunk:
            tr_count += 1
        if tr_count%self.columns != 0 and chunk in {"<tr>", "</tr>"}:
            continue
        final += chunk + "\n"
    return SafeString(final)

def get_grades_form(weights: list[str], columns: int):
    attrs = {}
    for weight in weights:
        for i in range(3):
            attrs[f'{weight}_{i}'] = forms.CharField(
                required=False,
                widget=forms.TextInput(attrs={'placeholder': 'points / total'})
            )
    
    attrs['as_table'] = _as_table
    attrs['columns'] = columns
    
    return type(
        'GradesForm',
        (forms.Form, ),
        attrs
    )