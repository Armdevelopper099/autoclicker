from tkinter import *
from tkinter import ttk
import pydirectinput
import time
from time import sleep
import keyboard
import threading

##############################################################################################################
app = Tk()
app.geometry('400x400')

##############################################################################################################
def start_def():
    while True:
        clickspeed = clickinput.get()
        keyboardb = keyinput.get()
        if keyboard.read_key() == keyboardb:
            pydirectinput.PAUSE = float(clickspeed)
            pydirectinput.click()

##############################################################################################################
#title
app.title("AutoClicker ArmoMan")
app.configure(background="black")

##############################################################################################################
#about click text
txtspeed = Label (app, text="Write the speed of clicks.  \nIf it is for example 10, it will do one  \nclick every 10 sec. If you want higher\n Click per second you can write 0.01\nor lower (ex:0.00002):", bg="black", fg="white", font="none 12 bold")
txtspeed.pack()

clickinput = Entry(app, width = 30)
clickinput.pack()

##############################################################################################################
#about key text
txtkey = Label (app, text="write the key (ex: a, b, c ...) that  \n you want to hold pressed to start the clicks:", bg="black", fg="white", font="none 12 bold")
txtkey.pack(pady=10)

keyinput = Entry(app, width = 30)
keyinput.pack()

##############################################################################################################

#start def
startbutton = ttk.Button(app, text="Start", command=threading.Thread(target=start_def).start())
startbutton.pack(pady=30)

##############################################################################################################

#stop the program
stopbutton = ttk.Button(app, text="Click to Stop", command=app.destroy)
stopbutton.pack(pady=2)

##############################################################################################################


app.mainloop()