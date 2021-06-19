from tkinter import *
from tkinter.ttk import Combobox


root = Tk()
root.title("National Lotto")
root.geometry("800x1000")
root.config(bg="yellow")

canvas=Canvas(root, width=590, height=320)
canvas.pack(side=TOP)
img =PhotoImage(file="daily.png")
canvas.create_image(0, 0, anchor=NW, image=img)



value_label = Label(root, text="Claim Your Reward Here!!!", font=("Arial", 25))
value_label.config(bg="white")
value_label.pack()

lblname=Label(root,text="Enter account holder name:", font=("Arial", 15))
lblname.config(bg="yellow")
lblname.place(x=80,y=400)

lblnumber=Label(root,text="Enter account number:", font=("Arial", 15))
lblnumber.config(bg="yellow")
lblnumber.place(x=80,y=480)

entry1=Entry(root,width=23)
entry1.place(x=380,y=400)
entry2=Entry(root,width=23)
entry2.place(x=380,y=480)

banks = Combobox(root)
banks.place()
banks["values"] = "Capitec", "ABSA", "FNB", "Nedbank", "Standard Bank", "Investec Bank"

value_label1 = Label(root, text="Select bank:", font=("Arial", 15))
value_label1.config(bg="yellow")
value_label1.place(x=80, y=560)
banks.place(x=380, y=560)

def clear_function():
    entry1.delete(0,END)
    entry2.delete(0,END)

def convert():
    import convert




tn2= Button(root, text="Clear", command=clear_function,font=("Arial", 15))
tn2.config(bg="green")
tn2.place(x=600, y=850)

btn_claim=Button(root,text="Claim",font=("Arial", 15))
btn_claim.config(bg="red")
btn_claim.place(x=400,y=850)

btn_conv=Button(root,text="Convert",command=convert, font=("Arial", 15))
btn_conv.config(bg="blue")
btn_conv.place(x=400,y=650)

root.mainloop()




