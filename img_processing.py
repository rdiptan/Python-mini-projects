import cv2 
import easygui
import numpy as np
import imageio 
import sys
import matplotlib.pyplot as plt 
import os
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image


top = Tk()
top.geometry('400x400')
top.title("CARTONIFY")
top.configure(background = 'white')
label = Label(top, background = "#CDCDCD", font=('calibri 20 bold'))


def upload():
    ImagePath = easygui.fileopenbox()
    Cartonify(ImagePath)

def Cartonify(ImagePath):
    originalImage = cv2.imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR.BGR2RGB)
    print(Image)

    if originalImage is NONE:
        print("CAN NOT FIND ANY IMAGE")
        sys.exit