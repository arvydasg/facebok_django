from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from . forms import forma
import pyautogui
import time                     # time library
import pyperclip                # copy paste allowing library
from openpyxl import Workbook, load_workbook # excel library
from django.views.generic import TemplateView
from . models import groups

BGBLACK = '\u001b[40m'
BGGREEN = '\u001b[42m'
BGRED = '\u001b[41m'
CEND = '\033[0m'

excel_file = load_workbook('facebook_groups.xlsx')
excel_sheet = excel_file['rajonai']

def test(request):
    # first, we import models into this view.
    # from . models import <model name>
    # then, we create a variable that stores a function from db? Like so.
    all_groups = groups.objects.all().count()
    veganai_groups = groups.objects.filter(group_category='veganai').count()
    dovanos_groups = groups.objects.filter(group_category='dovanos').count()

    # then, we put that variable into context variable, which then...
    context = {
        'all_groups': all_groups,
        'veganai_groups': veganai_groups,
        'dovanos_groups': dovanos_groups,
    }

    # is returned at the end. Context = context is the key.
    return render(request, 'main/test.html', context=context)
    # when that is done, I can then go to html templateview and do {{ context variable }}
    # and it prints out on the web! boom.
  
def homepage(request):
    my_form = forma()
    if request.method == "POST":
        my_form = forma(request.POST)
        if my_form.is_valid():
            '''
            Just getting some values for later use
            '''
            form_link = (my_form.cleaned_data['Link'])
            form_text = (my_form.cleaned_data['Text'])
            form_text2 = (my_form.cleaned_data['Text2'])
            form_number = (my_form.cleaned_data['Number'])
            form_category = (my_form.cleaned_data['Category'])
            print("\n")
            print("Dalykai kuriuos irasei yra:")
            print("LINK " + "= " + str( form_link))
            print("TEXT " + "= " + str( form_text))
            print("TEXT2 " + "= " + str( form_text2))
            print("Number " + "= " + str( form_number))
            print("Category " + "= " + str( form_category))
            print("\n")
            print("uz 5 sec procedura prasides")
            print("\n")
            time.sleep(5)

            '''
            FACEBOOK automation script starts NOW.
            After the user clicks "submit" on the front end - the script waits a few seconds for any user activity to stop before opening a new browser window.
            '''
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

            '''
            tracking count by setting 0 and adding +1 in each for loop run so in the end I can see how many groups the script has posted to and how long it took. 
            Interesting to track the duration to later see how minor changes in the code affects the time it takes for the script to complete. 
            Currently the average time for the script to post to one group is around 24 seconds. 
            Times that by 100 groups and you have 40 minutes that you can not do anything else with your computer. 
            If I manage to cut the those 24 seconds to 15 or so without any gliches (script stumbling over its own feet, because it goes too fast), then.. 
            yeah, better for me. Script finishes quickier.
            '''

            count = 0
            scriptoPradzia = time.time()
            
            '''
            okay, lets start the for loop
            '''
            
            for row in excel_sheet.iter_rows(max_row=int(form_number)):
                postoPradzia = time.time()
                group_url = row[1].value  # fetch group id from excel
                group_name = row[0].value # fetch group name from excel
                link = 'https://facebook.com/groups/'+str(group_url) # pro move
                # type group name
                time.sleep(3)
                pyperclip.copy(link)          # copies 'facebook.com/groups' and adds the group ID from excel sheet at the end of this url
                pyautogui.hotkey('ctrl', 'v') # pastes the FULL url
                pyautogui.typewrite('\n')     # press ENTER
                print("Atsidariau" + " " + BGBLACK + str(group_name) + CEND) # prints out in the console the name of the group it has opened
                print("\n")
                
                # let the browser window load
                print("9 seconds to let the browser window load")
                for i in range(10):
                    time.sleep(1)
                    print("Browser window load" + " " + str(i) + "/9")


                '''
                Looking for certain images in the 'resources' folder, then comparing an area on the screen to see if the images match anything on the screen.
                When it does - it clicks on that area. 
                In my case - the images are of a button that every group in facebook has. There are two types of buttons in facebook groups, so I am looking for both of them.
                And when one of those is found, I click on it. Now i am ready to paste in the text that I put in the FORM fields in the beginning.
                '''
                try:
                    x, y = pyautogui.locateCenterOnScreen("/home/arvydas/Dropbox/projects/facebook_automated_groups/resources/cpp.png")
                    print("The image 'create_public_post.png' was found.")
                    pyautogui.click(x,y)
                except TypeError:
                    print("Could not locate the image - Create a public post...")
                    a, b = pyautogui.locateCenterOnScreen("/home/arvydas/Dropbox/projects/facebook_automated_groups/resources/ws.png")
                    print("The image 'write something' was found")
                    pyautogui.click(a,b)

                '''
                Taking the inputs from the FORM that I submitted in the front end and pasting it in the 'facebook post box' that I opened in the last step.
                Some sleep in between the actions so the script wouldnt break for being too quick.
                '''
                time.sleep(2)
                pyperclip.copy(form_link)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'v') # paste
                pyautogui.hotkey('ctrl','a') # select all
                pyautogui.press('backspace') # link not necessary anymore, delete
                pyperclip.copy(form_text)
                pyautogui.hotkey('ctrl', 'v') # paste
                pyautogui.press('enter')      # newline
                pyperclip.copy(form_text2)
                pyautogui.hotkey('ctrl', 'v') # paste
                pyautogui.press('enter')      # newline

                '''
                After the text has been pasted, I can now click a few buttons to make the post clean, the buttons are currently being found by coordinates.
                In the future I should take pictures of those buttons and find them the way I did above in the code. 
                That would be a more fail proof way of clicking a button, since IF there is a lot of text in my post, the 'facebook post box' streches.
                As a result the buttons that I need to click using coordinates - move as well. 
                Then my script breaks.
                '''
                
                time.sleep(1)
                # f, o = pyautogui.locateCenterOnScreen("/home/arvydas/Dropbox/projects/facebook_automated_groups/resources/x.png")
                # pyautogui.click(f, o)
                # half(left) screen Acer Aspire V3 771G
                pyautogui.click(1664, 525) # turn off url link according to your screen pixel location (xdotool on linux)
                time.sleep(1)
                pyautogui.click(1448, 950) # Click POST according to your screen pixel location (xdotool on linux)

                                
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
                
            '''
            How long in TOTAL it took for the script to run and how many groups it posted to.
            '''
            print("Papostinau i" + " " + str(count) + " " + "grupes.") # how many groups I have posted to 
            print("Is viso uztruko {0} sekundes" .format(time.time() - scriptoPradzia)) # how long it took for the script to run
   
    context ={ 
        "form": my_form
    }

    return render(request, 'main/home.html', context) # How to render this page

# def success(request):
#     print("LINK " + "= " + str( form_link))
#     return render(request, 'main/success.html')
