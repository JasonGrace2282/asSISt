from django import forms


def get_grades_form(weights: list[str], rows: int = 3):
    textboxes = {}
    for weight in weights:
        for i in range(rows):
            textboxes[f'{i}__{weight}'] = forms.CharField()
    return type(
        'GradesForm',
        (forms.Form, ),
        textboxes
    )
