from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

root = Tk()
root.geometry = ("400 x 400")
root.resizable = (0,0)
root.config(bg='ghost white')
root.title('Text to Speech')

heading = Label(root, text="Test to Speech", font='arial 20 bold').pack()
Label(root, text="Enter Text", font='arial 15 bold').place(x=20, y=60)

Message = StringVar()

abc=Entry(root, textvariable=Message, width='100')
abc.place(x=20, y=100)


def TextToSpeech():
    Message=abc.get()
    speech = gTTS(text=Message)
    speech.save('test.mp3')
    playsound('test.mp3')
    os.remove('test.mp3')


def exit():
    root.destroy()


def reset():
    Message.set("")


Button(root, text="PLAY", font='arial 15 bold', command=TextToSpeech, width=4).place(x=25, y=200)
Button(root, text="EXIT", font='arial 15 bold', command=exit, width=4, bg='OrangeRed1').place(x=100, y=200)
Button(root, text="RESET", font='arial 15 bold', command=reset, width=4).place(x=175, y=200)


root.mainloop()
