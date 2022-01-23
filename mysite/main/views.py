from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from .forms import forma
import pyautogui

def homepage(request):
    my_form = forma()
    if request.method == "POST":
        my_form = forma(request.POST)
        if my_form.is_valid():
            link = (my_form.cleaned_data['Link'])
            print(my_form.cleaned_data)
            print(link)         # how to pass this value to another function???
            return HttpResponseRedirect('/run')
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
