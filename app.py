import pkg_resources.py2_warn
import tkinter as tk
from tkinter import * #needed for the graphical user interface
import pyautogui #needed for screenshot and image recognition
import pydirectinput #needed to execute keyboard commands
from PIL import Image, ImageTk #needed to process external images from URL's
import requests #needed for image URL's
from io import BytesIO #needed for image URL's
import time
from tkinter import messagebox
print("DO NOT CLOSE THIS TERMINAL. Keep this terminal open, it will tell you some useful information.\n")
print("Please make sure you ran program in administrator mode or else the program can't click for you.\n")
print("also make sure you click back on your game to focus on the game. Cheers ~ Matt1331")


root = Tk()
tracking_var = False

response110x70 = requests.get("https://raw.githubusercontent.com/matter13311/FS2AutoAFK/master/READY110x70.png")
response130x80 = requests.get("https://raw.githubusercontent.com/matter13311/FS2AutoAFK/master/READY130x80.png")
response95x60 = requests.get("https://raw.githubusercontent.com/matter13311/FS2AutoAFK/master/READY95x60.png")

start110x70 = requests.get("https://raw.githubusercontent.com/matter13311/FS2AutoAFK/master/START110x70.png")
start130x80 = requests.get("https://raw.githubusercontent.com/matter13311/FS2AutoAFK/master/START130x80.png")
start95x60 = requests.get("https://raw.githubusercontent.com/matter13311/FS2AutoAFK/master/START95x60.png")

start_img_110x70 = Image.open(BytesIO(start110x70.content))
start_img_130x80 = Image.open(BytesIO(start130x80.content))
start_img_95x60 = Image.open(BytesIO(start95x60.content))

img_110x70 = Image.open(BytesIO(response110x70.content))
img_130x80 = Image.open(BytesIO(response130x80.content))
img_95x60 = Image.open(BytesIO(response95x60.content))

def quickRefresh():
    x, y = pyautogui.position()
    pyautogui.moveTo(960, 540)
    pyautogui.click()
    pyautogui.moveTo(x, y)


#this function will go through all images, that vary slightly, and attempt to find it on your screen.
#these images are grabbed from online to minimize program size. It used to be 400mb, now it's 33mb.
def checkStart():

    try:
        x, y = pyautogui.locateCenterOnScreen(img_110x70,  confidence=0.8)
    except TypeError:
        #print("no ready image found1")
        try:
            x, y = pyautogui.locateCenterOnScreen(img_130x80,  confidence=0.8)
        except TypeError:
            #print("no ready image found2")
            try:
                x, y = pyautogui.locateCenterOnScreen(img_95x60,  confidence=0.8)
            except TypeError:
                print("no ready image found3")
                try:
                    x, y = pyautogui.locateCenterOnScreen(start_img_110x70, confidence=0.8)
                except TypeError:
                    #print("no start image found1")
                    try:
                        x, y = pyautogui.locateCenterOnScreen(start_img_130x80, confidence=0.8)
                    except TypeError:
                        #print("no start image found2")
                        try:
                            x, y = pyautogui.locateCenterOnScreen(start_img_95x60, confidence=0.8)
                        except TypeError:
                            print("no start image found3")
                        else:
                            print("start found3")
                            print("x:", x)
                            print("y:", y)
                            pyautogui.moveTo(pyautogui.locateCenterOnScreen(start_img_95x60, confidence=0.8))
                            pyautogui.click()
                    else:
                        print("start found3")
                        print("x:", x)
                        print("y:", y)
                        pyautogui.moveTo(pyautogui.locateCenterOnScreen(start_img_130x80, confidence=0.8))
                        pyautogui.click()
                else:
                    print("start found3")
                    print("x:", x)
                    print("y:", y)
                    pyautogui.moveTo(pyautogui.locateCenterOnScreen(start_img_110x70, confidence=0.8))
                    pyautogui.click()
            else:
                print("ready found3")
                print("x:", x)
                print("y:", y)
                pyautogui.moveTo(pyautogui.locateCenterOnScreen(img_95x60,  confidence=0.8))
                pyautogui.click()
        else:
            print("ready found2")
            print("x:", x)
            print("y:", y)
            pyautogui.moveTo(pyautogui.locateCenterOnScreen(img_130x80,  confidence=0.8))
            pyautogui.click()
    else:
        print("ready found1")
        print("x:", x)
        print("y:", y)
        pyautogui.moveTo(pyautogui.locateCenterOnScreen(img_110x70,  confidence=0.8))
        pyautogui.click()


#this function is a loop that will keep executing as long as the button on the GUI is turned on
def loop(toggle=False):
    global tracking_var
    if toggle:
        if tracking_var:
            label1.config(text="Program is NOT running")
            button2.config(text="Turn On")
            tracking_var = False
        else:

            label1.config(text="Program is running")
            button2.config(text="Turn Off")
            tracking_var = True

    if tracking_var:
        if var.get() == 0:
            checkStart()
            if len(entry_widget.get()) == 0:  # if the input box is empty, it'll default to pressing W.
                print("nothing in box, default is w")
                pydirectinput.press('w')
            else:
                pydirectinput.press(
                    entry_widget.get())  # if there is something inside the input box, make the computer continously press the key

            root.after(2500, loop)  # 2500 is equivalent to 2.5 seconds. This means every 2.5 seconds, the program will execute all functions and loops again.
        else:
            quickRefresh()
            if len(entry_widget.get()) == 0:  # if the input box is empty, it'll default to pressing W.
                print("nothing in box, default is w")
                pydirectinput.press('w')
            else:
                pydirectinput.press(
                    entry_widget.get())  # if there is something inside the input box, make the computer continously press the key

            root.after(5000, loop)  # 2500 is equivalent to 2.5 seconds. This means every 2.5 seconds, the program will execute all functions and loops again.




#This function is used to limit the amount of characters inside the input box.wwwww
def character_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[-1])

def messagePrompt():
    messagebox.showinfo(title="Quick Refresh", message="You would use quick refresh if you want to keep using your computer while having FS2 running. It will disable auto-ready/start, and automatically make you click on the game every few seconds. It will then place your cursor back to where it was originally")


root.title('FS2 AFKBOT') #sets program title
root.iconbitmap('images/prem.ico') #sets program icon
root.geometry("300x400") #sets program GUI size

label1 = Label(root, text="Program is NOT running") #text label
label1.pack(pady=5)

button2 = Button(root, text="Turn On", command=lambda: loop(True)) #button that turns on or off the loop
button2.pack()


inputFieldFrame = Frame(root) #adds a Frame inside the GUi to better organize everything
inputFieldFrame.pack()

label2 = Label(inputFieldFrame, text="Enter key that you want spammed: ")
label2.pack(side=LEFT, pady=10)

entry_text = StringVar() # the text in  your entry
entry_widget = Entry(inputFieldFrame, width=2, textvariable=entry_text)#the entry
entry_widget.insert(0, "w")
entry_widget.pack(side=LEFT)

label3 = Label(root, text="If the program can't find the start or ready button,\n make sure it's not fullscreen and \n try changing to different game resolution")
label3.pack(pady=30)

entry_text.trace("w", lambda *args: character_limit(entry_text))

var = IntVar()
checkbox1 = Checkbutton(root, text='Check to enable auto-refresher', variable=var)
checkbox1.pack()

label4 = Label(root, text="Enter refresh rate of auto-refresher in ms: ")
label4.pack()

button3 = Button(root, width=1, height=1, text="i", command=messagePrompt)
button3.pack()





my_img = ImageTk.PhotoImage(Image.open("images/ai.png"))
my_label = Label(image=my_img)
my_label.pack()



gitHub_label = Label(text="https://github.com/matter13311/FS2AutoAFK")
gitHub_label.pack()


root.mainloop()