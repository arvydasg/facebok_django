from django.shortcuts import render
from django.http import HttpResponse

from django import forms
from .forms import RawProductForm

def homepage(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            # now the data is good
            labukas = (my_form.cleaned_data['title'])
            print(labukas)
        else:
            print(my_form.errors)
            
    context = {
        "form": my_form
    }
    return render(request, 'main/home.html', context)
