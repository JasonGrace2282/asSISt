from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control"}),
        max_length=100
    )
    domain = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "sisstudent.fcps.edu/SVUE", "class": "form-control mb-3"})
    )
