from django import forms


class ChooseClass(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['class'] = forms.ChoiceField(
            choices=[
                (subject.id, subject.name)
                for subject in user.subjects.all()
            ],
            widget=forms.RadioSelect(attrs={'class': 'class-radio'}),
        )
