from django import forms

GRUPIU_KATEGORIJOS= [
    ('didieji', 'Didieji - 35 grupės'),
    ('rajonai', 'Rajonai - 42 grupės'),
    ('skelbimai', 'Skelbimai - 42 grupės'),
    ('mamytes', 'Mamytės - 13 grupių'),
    ('veganai', 'Veganai - 10 grupių'),
    ('dovanos', 'Dovanos - 10 grupių'),
    ]

class forma(forms.Form):
    Link = forms.CharField(label = "Facebook posto nuoroda")
    Text = forms.CharField(label = "Pagrindinis CTA sakinys")
    Text2 = forms.CharField(label = "Aplankyk puslapį CTA + nuoroda")
    Number = forms.DecimalField(label = "I kiek grupiu nori papostinti?")
    Category= forms.CharField(label='Į kokią kategoriją norėtum postinti?', widget=forms.Select(choices=GRUPIU_KATEGORIJOS))

