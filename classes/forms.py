from django import forms


class ChooseClass(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['class'] = forms.ChoiceField(
            choices=[
                (subject.id, subject.name)
                for subject in self.account.subjects.all()
            ]
        )
