from django import forms

class forma(forms.Form):
    Link = forms.CharField()
    Text = forms.CharField()
    Amout = forms.DecimalField()
