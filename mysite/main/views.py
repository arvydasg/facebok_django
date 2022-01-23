from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .forms import RawProductForm
import pyautogui


def homepage(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            labukas = (my_form.cleaned_data['title'])
            print(my_form.cleaned_data)
            print(labukas)
        else:
            print(my_form.errors)
            
    context = {
        "form": my_form
    }

    return render(request, 'main/home.html', context)

def run(request):
    # opens new tab in chrome
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('t')
    pyautogui.keyUp('t')
    pyautogui.keyUp('ctrl')
    print("hello world")        # prints in terminal
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""") # reloads the page basically

# # Test page
# def run(request):
#     return render(request, 'main/run.html')
