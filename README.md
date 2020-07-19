# FS2AutoAFK
A program that automatically lets you start matches to grind out the new 3x3 gamemode in Freestyle 2


How it works:
The program scans your screen for anything that looks like the FS2 "ready" or "start" button.
If it finds this on your screen, it will move your cursor to the picture, and then execute a left click.


Disclaimer:
1. The program will only scan your primary monitor. So if you have two monitors, make sure the game is on the primary monitor.
1. If the program can't find the ready button or start button, try changing your game resolution to something different.
1. Don't spam click the turn on/ turn off button when it seems to be frozen. 
1. Because the program will control your cursor and execute left clicks for you, some anti-virus will think this as a virus. However,
the source code for the program can be viewed at my github, where you can try to execute the code yourself with python.

To build the program, simply download app.py and also everything inside the images folder. There is no need to download any of the READY or START png images. 
After that, just execute python app.py to run.


### Things to add in the future
1. Make it so that users can add their own custom images for the program to scan for


- matt1331
