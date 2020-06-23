import pkg_resources.py2_warn
import tkinter as tk
from tkinter import *
import pyautogui
import pydirectinput
from PIL import Image, ImageTk
import requests
from io import BytesIO

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

def checkStart():
    try:
        x, y = pyautogui.locateCenterOnScreen(img_110x70,  confidence=0.8)
    except TypeError:
        print("no ready image found1")
        try:
            x, y = pyautogui.locateCenterOnScreen(img_130x80,  confidence=0.8)
        except TypeError:
            print("no ready image found2")
            try:
                x, y = pyautogui.locateCenterOnScreen(img_95x60,  confidence=0.8)
            except TypeError:
                print("no ready image found3")
                try:
                    x, y = pyautogui.locateCenterOnScreen(start_img_110x70, confidence=0.8)
                except TypeError:
                    print("no start image found1")
                    try:
                        x, y = pyautogui.locateCenterOnScreen(start_img_130x80, confidence=0.8)
                    except TypeError:
                        print("no start image found2")
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
        if len(entry_widget.get()) == 0:
            print("nothing in box, default is w")
            pydirectinput.press('w')
        else:
            pydirectinput.press(entry_widget.get())
        checkStart()
        root.after(2500, loop)

def character_limit(entry_text):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[-1])

root.title('FS2 AFKBOT')
root.iconbitmap('images/prem.ico')
root.geometry("300x350")

label1 = Label(root, text="Program is NOT running")
label1.pack(pady=10)

button2 = Button(root, text="Turn On", command=lambda: loop(True))
button2.pack()


inputFieldFrame = Frame(root)
inputFieldFrame.pack()

label2 = Label(inputFieldFrame, text="Enter key that you want spammed: ")
label2.pack(side=LEFT)

entry_text = StringVar() # the text in  your entry
entry_widget = Entry(inputFieldFrame, width=2, textvariable=entry_text)#the entry
entry_widget.insert(0, "w")
entry_widget.pack(side=LEFT)

label3 = Label(root, text="If the program can't find the start or ready button,\n make sure it's not fullscreen and \n try changing to different game resolution")
label3.pack(pady=30)

entry_text.trace("w", lambda *args: character_limit(entry_text))



my_img = ImageTk.PhotoImage(Image.open("images/ai.png"))
my_label = Label(image=my_img)
my_label.pack()

gitHub_label = Label(text="https://github.com/matter13311/FS2AutoAFK")
gitHub_label.pack()


root.mainloop()