from tkinter import *

from tkinter import simpledialog, messagebox, Spinbox

root = Tk()
root.title("National Lotto")
root.geometry("700x800")
root.config(bg="red")

import random

def lotto_numbers():
    lot_num = set()

    for i in range(0,6):
      number1 = random.randint(1,49)

      while number1 in lot_num:
          number1 = random.randint(1,49)

      lot_num.add(number1)

    lblanswer.config(text=str("The Lottery numbers are:\n"+str(lot_num)))

    counter = 0

num1=IntVar()
num2=IntVar()
num3=IntVar()
num4=IntVar()
num5=IntVar()
num6=IntVar()

canvas=Canvas(root, width=200, height=200)
canvas.pack(side=TOP)
img =PhotoImage(file="lotto(1).png")
canvas.create_image(0, 0, anchor=NW, image=img)

entry1=Spinbox(root, from_=1, to=49, textvariable=num1, width=5)
entry1.place(x=240, y=350)

entry2=Spinbox(root, from_=1, to=49, textvariable=num2, width=5)
entry2.place(x=170, y=350)

entry3=Spinbox(root, from_=1, to=49, textvariable=num3, width=5)
entry3.place(x=310, y=350)

entry4=Spinbox(root, from_=1, to=49,textvariable=num4, width=5)
entry4.place(x=380, y=350)

entry5=Spinbox(root, from_=1, to=49,textvariable=num5, width=5)
entry5.place(x=450, y=350)

entry6=Spinbox(root, from_=1, to=49,textvariable=num6, width=5)
entry6.place(x=520, y=350)

lbl = Label(root, text="Please enter your  6 number from 1-49")
lbl.config(bg="yellow")
lbl.place(x=260, y=300)



lblanswer = Label(root, height=10, width=65)
lblanswer.place(x=100, y=450)

lbllucky = Label (text="", font="arial 12")
lbllucky.place(x=275, y=420)
lbllucky.config(bg="green")

row1 = [int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()),int(entry5.get()), int(entry6.get()) ]
row2=lotto_numbers

compare = (set(row1).intersection(set(row2)))
results = len (compare)
def clear_function():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)
    entry6.delete(0,END)


def exit():
    msg_box= messagebox.askquestion('exit application',"are you sure you want to exit the application?", icon="warning")
    if msg_box == "yes":
        root.destroy()
        import main.py





    else:
        messagebox.showinfo('Return', "You will now return to the app", icon="warning")




exit_btn = Button(text = "quit", command=exit)
exit_btn.config(bg="green")
exit_btn.place(x=630, y=750)

tn2= Button(root, text="Clear", command=clear_function)
tn2.config(bg="green")
tn2.place(x=500, y=750)


play_btn = Button( root,text ="Play", command=lotto_numbers)
play_btn.config(bg="green")
play_btn.place(x=330, y=630)





root.mainloop()
