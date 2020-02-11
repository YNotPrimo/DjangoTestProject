from django import forms


class FormName(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
