from django import forms

class forma(forms.Form):
    Link = forms.CharField()
    Text = forms.CharField()
    Text2 = forms.CharField()
    Number = forms.DecimalField()
    Category= forms.CharField()
