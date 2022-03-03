"""
Patvarkytas 02-23.

This.
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from main.forms import forma
import pyautogui
import time
import pyperclip                # copy paste allowing library
from openpyxl import Workbook, load_workbook # excel library
from django.views.generic import TemplateView
from main.models import groups

import cv2

BGBLACK = '\u001b[40m'
BGGREEN = '\u001b[42m'
BGRED = '\u001b[41m'
CEND = '\033[0m'

def veganai(request):
    my_form = forma()
    if request.method == "POST":
        my_form = forma(request.POST)
        if my_form.is_valid():
            form_link = (my_form.cleaned_data['Link'])
            form_text = (my_form.cleaned_data['Text'])
            form_text2 = (my_form.cleaned_data['Text2'])
            print("\n")
            print("Dalykai kuriuos irasei yra:")
            print("LINK " + "= " + str( form_link))
            print("TEXT " + "= " + str( form_text))
            print("TEXT2 " + "= " + str( form_text2))
            print("\n")
            print("uz 5 sec procedura prasides")
            print("\n")
            time.sleep(5)

            print("3 Seconds to prepare the browser")
            for i in range(4):
                time.sleep(1)
                print("Prepare browser" + " " + str(i) + "/3")
            time.sleep(1)
            print("Opening browser")
            time.sleep(1)
            print("\n")
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('t')
            pyautogui.keyUp('t')
            pyautogui.keyUp('ctrl')

            count = 0
            scriptoPradzia = time.time()

            # using database items instead of excel file like before
            items = groups.objects.filter(group_category='veganai')
            for item in items.values('group_name', 'group_link', 'group_category'):
                postoPradzia = time.time()
                group_name = item['group_name']
                group_link = item['group_link']
                group_category = item['group_name']
                
                link = 'https://facebook.com/groups/'+str(group_link) # pro move
                time.sleep(3)
                pyperclip.copy(link)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.typewrite('\n')
                print("Atsidariau" + " " + BGBLACK + str(group_name) + CEND)
                print("\n")
                
                # let the browser window load
                print("9 seconds to let the browser window load")
                for i in range(10):
                    time.sleep(1)
                    print("Browser window load" + " " + str(i) + "/9")
                
                try:
                    x, y = pyautogui.locateCenterOnScreen("/home/arvydas/Desktop/test/cpp.png", confidence=0.9)
                    print("The image 'create_public_post.png' was found.")
                    pyautogui.click(x,y)
                except TypeError:
                    print("Could not locate the image - Create a public post...")
                    a, b = pyautogui.locateCenterOnScreen("/home/arvydas/Desktop/test/ws.png", confidence=0.9)
                    print("The image 'write something' was found")
                    pyautogui.click(a,b)

                time.sleep(2)
                pyperclip.copy(form_link)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.hotkey('ctrl','a')
                pyautogui.press('backspace')
                pyperclip.copy(form_text)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
                pyperclip.copy(form_text2)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')

                time.sleep(1)
                a, c = pyautogui.locateCenterOnScreen("/home/arvydas/Dropbox/src/facebook_django/static/resources/x.png", confidence=0.9)
                pyautogui.click(a,c)
                time.sleep(1)
                f, g = pyautogui.locateCenterOnScreen("/home/arvydas/Dropbox/src/facebook_django/static/resources/post.png", confidence=0.9)
                pyautogui.click(f,g)

                                
                # some time to prepare the browser
                print("2 Seconds to prepare the browser")
                for i in range(2):
                    time.sleep(1)
                    print("Posting" + " " + str(i) + "/2")
                    time.sleep(1)
                pyautogui.write(['f6'])     # mark search field, prepare for new link input
                print(BGGREEN + "PAPOSTINTA"+ CEND+ " i " + " " + BGBLACK + str(group_name)+"."+" " + BGRED + "Uztruko {0} sekundes" .format(time.time() - postoPradzia) + CEND)
                print("--------------------------------------------------------------------------------------")
                print("\n")       # new line
                count +=1 # variable will increment every loop iteration
                
            print("Papostinau i" + " " + str(count) + " " + "grupes.") # how many groups I have posted to 
            print("Is viso uztruko {0} sekundes" .format(time.time() - scriptoPradzia)) # how long it took for the script to run
   
    context ={ 
        "form": my_form
    }

    return render(request, 'main/veganai.html', context) # How to render this page
