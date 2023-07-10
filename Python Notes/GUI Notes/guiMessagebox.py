from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title="INFO", message="Message for you")
    messagebox.showwarning(title="WARNING", message="You have a virus")
    messagebox.showerror(title="ERROR", message="Something wrong")

    if messagebox.askokcancel(title="ASK OK CANCEL", message="Do you want to do thing"):
        messagebox.showinfo(title="GOOD JOB", message="You did a thing")
    else:
        messagebox.showinfo(title="LAZY", message="You didn't do a thing")

    if messagebox.askretrycancel(title="RETRY CANCEL", message="Do you want to try again"):
        messagebox.showinfo(title="GOOD JOB", message="You tried")
    else:
        messagebox.showinfo(title="LAZY", message="You didn't try")

    if messagebox.askyesno(title="YES OR NO", message="Do you like cake"):
        messagebox.showinfo(title="THANKS", message="Thank you")
    else:
        messagebox.showinfo(title=":(", message="I will try my best next time")

    answer = messagebox.askquestion(title="ASK QUESTION", message="Do you like pie")
    if answer == "yes":
        messagebox.showinfo(title="GOOD", message="I like too")
    else:
        messagebox.showinfo(title="BAD", message="Why didn't you like")

    print(messagebox.askyesnocancel(title="Yes No Cancel", message="Do you like code?", icon="info"))
    answer2 = messagebox.askyesnocancel(title="Yes No Cancel", message="Do you like code?")
    if answer2 == True:
        print("You like the code :)")
    elif answer2 == False:
        print("Then why are you looking at code")
    else:
        print("You dodged the question")

window = Tk()

button = Button(window, command=click, text="Click Me")
button.pack()

window.mainloop()