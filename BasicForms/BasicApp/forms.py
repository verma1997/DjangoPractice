from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    text = forms.CharField(widget = forms.Textarea)
