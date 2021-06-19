from tkinter import *
from tkinter import messagebox
import rsaidnumber
from datetime import date
from dateutil.relativedelta import relativedelta




root = Tk()
root.title("National Lotto")
root.geometry("500x560")
root.config(bg="yellow")


entry1=Entry(root, width=23)
entry1.place(x=270, y=200)
entry2=Entry(root, width=23)
entry2.place(x=270, y=100)
entry3=Entry(root, width=23)
entry3.place(x=270, y=300)


lbltext = Label(text="no under 18 are allowed to play")
lbltext.config(bg="red", font='bold')
lbltext.place(x=100, y=25)

lblname = Label(root, text="Enter your email:")
lblname.place (x=50, y=200)

lblsurname= Label(root, text="Enter your name:")
lblsurname.place(x=50, y=100)
lblid=Label(root,text="Enter your id number:")
lblid.place(x=50, y=300)

def entry1():
    if eval(entry1.get()) != str(entry1.get()):
        messagebox.showerror("Error", "Please enter your Fullname")

    elif entry1 == " ":
        messagebox.showerror("Error", "Enter correct details")

    else:
        messagebox.showinfo("Correct info given")


def verify():
    try:

        id_number = rsaidnumber.parse(entry3.get())
        birth_date = id_number.date_of_birth
        real_age = relativedelta(date.today(), birth_date.date())
        real_age = real_age.years

        if len(entry3.get()) != 13:
            messagebox.showerror("Error", "Please enter correct ID number")
        elif id_number == " ":
            messagebox.showerror("Error", "Enter correct details")

        elif real_age >= 18:
            real_age = str(real_age)
            messagebox.showinfo("You are " + real_age + " years old", "You can play")



            root.destroy()

            import main2

        else:
            messagebox.showinfo("You're not old enough", "")

    except ValueError:

        messagebox.showerror("", "")



def exit():
    msg_box= messagebox.askquestion('exit application',"are you sure you want to exit the application?", icon="warning")
    if msg_box=="yes":
        root.destroy()
    else:
        messagebox.showinfo('Return', "You will now return to the app", icon="warning")


exit_btn = Button(text = "Quit", command=exit)
exit_btn.config(bg="green")
exit_btn.place(x=400, y=450)


verify_btn=Button(text="verify", command= verify)
verify_btn2=Button(command= entry1)
verify_btn.config(bg="green")
verify_btn.place(x=200, y=450)

root.mainloop()

