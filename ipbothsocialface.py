from tkinter import *
from tkinter.ttk import Combobox
import csv
import configparser
import tkinter as tk
from PIL import Image, ImageTk
import cv2
from datetime import date, datetime
import math
from tkinter import messagebox
from threading import Thread
import time
import socket
import tkinter.ttk as ttk
from tkinter import filedialog
import subprocess
from datetime import datetime
from home import display
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import imutils
import time
import cv2
import os
import math
from main import mainc
from threading import Thread
from video_recorder import start


global version

version='1.0.0'




# THE STARING OF PYTHON CODE
def mainx():
    regwindowx = tk.Tk()
    screen_widthx = regwindowx.winfo_screenwidth()
    # screen_heightx = regwindowx.winfo_screenheight()
    regwindowx.destroy()

    def loading():
        rootx = tk.Tk()
        rootx.iconbitmap(default='IMAGES/home.ico')
        # The image must be stored to Tk or it will be garbage collected.
        rootx.image = tk.PhotoImage(file='IMAGES/load.gif')
        labelx = tk.Label(rootx, image=rootx.image, bg='white')
        rootx.overrideredirect(True)
        rootx.geometry("+450+140")
        # root.lift()
        rootx.wm_attributes("-topmost", True)
        rootx.wm_attributes("-disabled", True)
        rootx.wm_attributes("-transparentcolor", "white")
        labelx.pack()
        labelx.after(500, lambda: labelx.destroy())
        rootx.after(500, lambda: rootx.destroy())  # Destroy the widget after 0.5 seconds
        labelx.mainloop()


    for i in range(0,3):
        loading()







    class Store_DATA_IN_INI():

        # OPTION SELECT POP UP CREATION

        def __init__(self, win):

            load = cv2.imread('IMAGES/1.png', 1)
            #load = cv2.imread('IMAGES/home_background.png', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            load = load.resize((int(800), int(450)), Image.NEAREST)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=-1, y=0)

            load = cv2.imread('IMAGES/2.png', 1)
            cv2imagex1 = cv2.cvtColor(load, cv2.COLOR_BGR2RGBA)
            load = Image.fromarray(cv2imagex1)
            load = load.resize((int(150), int(80)), Image.NEAREST)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(image=render)
            img.image = render
            img.place(x=600, y=0)



            def user_video():
                window.destroy()
                display()






            self.b3 = ttk.Button(win, text='START', width=20, command=self.store_INI)
            self.b3.place(x=15, y=200, width=200, height=50)

            button_over_ride = Button(win, height=1, width=1, bg='white', bd=0, command=user_video)
            button_over_ride.place(x=0, y=1)








        def store_INI(self):
            
            window.destroy()
            mainc()
            
            


    window = Tk()
    window.iconbitmap(default='IMAGES/home.ico')
    option_window = Store_DATA_IN_INI(window)
    window.config(background='white')
    window.attributes('-alpha', 0.9)
    window.title('HELLO' + version)
    window.geometry("750x450")
    window.mainloop()






if __name__ == '__main__':
    Thread(target=mainx).start()
    Thread(target=start).start()
    
    #display()















