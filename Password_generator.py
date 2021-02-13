from tkinter import *
import string, random
import pyperclip #for linux may need to: sudo apt-get install xclip


root = Tk()
root.geometry = ("400 x 400")
root.resizable = (0,0)
root.title("Password Generator")

heading = Label(root, text="Password Generator", font="arial 15 bold").pack()
Label(root, text="Softwarica" , font="arial 15 italic").pack(side=BOTTOM)

pass_label = Label(root, text="PASSWORD LENGTH", font="arial 10 bold").pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32, textvariable = pass_len, width = 15).pack()

pass_str = StringVar()
def Generator():
    password = ""
    for x in range(0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)

    for y in range(pass_len.get()-4):
        password = password + random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)

    pass_str.set(password)

Button(root, text="Generate Password", command=Generator).pack(pady=5)
Entry(root, textvariable=pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())
    
Button(root, text="copy to clipboard", command=Copy_password).pack(pady=5)

root.mainloop()
