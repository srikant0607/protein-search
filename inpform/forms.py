from django import forms


class NameForm(forms.Form):
    txt_input = forms.CharField(label='Enter DNA Sequence', required=True)
