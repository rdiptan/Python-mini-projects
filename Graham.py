from tkinter import *
import math

root = Tk()
root.geometry('500x300')
root.title("Graham Formula")

price = StringVar()
eps = StringVar()
book = StringVar()
result = StringVar()
verdict = StringVar()


def Exit():
    root.destroy()


def Reset():
    price.set("")
    eps.set("")
    book.set("")
    result.set("")
    verdict.set("")


def Result():
    a = float(eps.get())
    b = float(book.get())
    p = float(price.get())
    res = round((math.sqrt(22.5*a*b)), 2)
    result.set(str(res))

    

    if p>res:
        verdict.set("Over Valued: "+ str(round((p-res),2)) + " ~ " + str(round(((p-res)/p*100), 2)) + "%")
    else:
        verdict.set("Under Valued: "+ str(round((res-p),2)) + " ~ " + str(round(((res-p)/p*100), 2)) + "%")

Label(root, font='arial 12 bold', text='Market Price').place(x=60, y=30)
Entry(root, font='arial 10', textvariable=price,
      bg='ghost white').place(x=190, y=30)

Label(root, font='arial 12 bold', text='EPS').place(x=60, y=60)
Entry(root, font='arial 10', textvariable=eps,
      bg='ghost white').place(x=190, y=60)

Label(root, font='arial 12 bold', text='Book value').place(x=60, y=90)
Entry(root, font='arial 10', textvariable=book,
      bg='ghost white').place(x=190, y=90)

Button(root, font='arial 10 bold', text='Calculate Price',
       padx=2, bg='LightGray', command=Result).place(x=60, y=120)
Entry(root, font='arial 12 bold', textvariable=result, width="30",
      bg='ghost white', state="readonly").place(x=190, y=120)
Entry(root, font='arial 12 bold', textvariable=verdict, width="30",
      bg='ghost white', state="readonly").place(x=190, y=150)

Button(root, font='arial 10 bold', text='RESET', width=6,
       command=Reset, bg='LimeGreen', padx=2).place(x=80, y=190)
Button(root, font='arial 10 bold', text='EXIT', width=6, command=Exit,
       bg='OrangeRed', padx=2).place(x=180, y=190)

root.mainloop()
