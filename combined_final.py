from tkinter import *
from tkinter.ttk import *
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import tkinter as tk
import time
import os
import requests
import cv2
window = Tk()

window.title("WELCOME")
#window.config(bg="green")
window.geometry('700x590')
window.config(background="darkblue")

lbl = Label(window, text="SOCIAL DISTANCE VOILATION DETECTION SYSTEM")
lbl.place(x=10, y=8)

lbl.config(font=("times-bold-italic", 20), )

lbl.config(background="yellow")


# lbl.grid(column=2, row=1)

def disable_event():
    pass


def facem():
    tkinter.messagebox.showinfo("Welcome to Face Mask Detector.", "You are about to perform Face Mask Detection       "
                                                                  "                                      press "
                                                                  "ok to continue              and              press "
                                                                  "'q' to Quit")
    os.system('python newfacemask.py -n prn')


def sociald():
    tkinter.messagebox.showinfo("Welcome to Social Distance Detector.", "You are about to perform Social Distance "
                                                                        "Detection                                    "
                                                                        "  press "
                                                                        "ok to continue           and          press "
                                                                        "'q' to Quit")
    os.system('python ipsocial.py')


def facesocial():
    tkinter.messagebox.showinfo("Welcome to Both Face Mask and Social Distance Detector.", "You are about to perform "
                                                                                           "Both Face Mask and Social "
                                                                                           "Distance Detection        "
                                                                                           "     press "
                                                                                           "ok to continue         and "
                                                                                           "          press "
                                                                                           "'q' to Quit")
    os.system('python ipbothsocialface.py')


def imform():
    
    tkinter.messagebox.showinfo("info about the project","A Computer Vision based solution to check if people follow social distancing norms, wear a mask, or if they are roaming out! Social Distancing Analyser automatically detects the extent to which social distancing protocols are followed in the area. Deploying it on current surveillance systems and drones used by police to monitor large areas can help to prevent coronavirus by allowing automated and better tracking of activities happening in the area. It shows analytics of the area in real time. It can also be used to alert police in case of considerable violation of social distancing protocols in a particular area.")
    print("Done")


def autom():
    tkinter.messagebox.showinfo("Welcome to video surveillance.", "You are about to perform "
                                                                            "Detection in video "
                                                                            "press "
                                                                            "ok to continue              and          "
                                                                            "    press "
                                                                            "'q' to Quit")
    os.system('python video.py')


imagetest = PhotoImage(file="comimg/facereg.png")
imagetest1 = PhotoImage(file="comimg/social.png")
imagetest2 = PhotoImage(file="comimg/bothfi.png")
imagetest3 = PhotoImage(file="comimg/infrmm.png")
imagetest4 = PhotoImage(file="comimg/automatic.png")
imagetest5 = PhotoImage(file="comimg/quitt.png")

bt1 = Button(window, compound="top", text="SOCIAL DISTANCING FROM IMAGE", image=imagetest1, command=sociald)
bt1.place(x=40, y=280)
# bt1.grid(column=1, row=8)
# bt1.pack()

bt2 = Button(window, compound="top", text="FACE MASK FROM IMAGE", image=imagetest, command=facem)
bt2.place(x=40, y=50)
# bt2.grid(column=1, row=4)

bt3 = Button(window, compound="top", text="LIVE DETECTION", image=imagetest2, command=facesocial)
bt3.place(x=250, y=50)
#bt3.grid(column=4, row=4)

bt4 = Button(window, compound="top", text="ABOUT THE PROJECT", image=imagetest3, command=imform)
bt4.place(x=250, y=280)
#bt4.grid(column=2, row=4)

bt5 = Button(window, compound="top", text="VIDEO SURVEILLANCE", image=imagetest4, command=autom)
bt5.place(x=460, y=50)
# bt5.grid(column=2, row=8)

bt6 = Button(window, compound="top", text="QUIT", image=imagetest5, command=quit)
bt6.place(x=460, y=280)
# bt6.grid(column=3, row=8)

window.resizable(0, 0)
window.protocol("WM_DELETE_WINDOW", disable_event)
window.mainloop()