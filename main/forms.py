"""
blabla bla.

bla
"""

from django import forms


class forma(forms.Form):
    Link = forms.CharField()
    # Text = forms.CharField()
    Text = forms.CharField(
        widget=forms.Textarea(attrs={"name": "body", "style": "height: 3em;"})
    )
    Text2 = forms.CharField()
    # Number = forms.DecimalField()
    # Category= forms.CharField()


print
