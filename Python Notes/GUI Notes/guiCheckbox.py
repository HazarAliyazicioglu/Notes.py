from tkinter import *

window = Tk()

def display():
    if(x.get()==1):
        print("You agree")
    else:
        print("Tou dont agree")

# x değişkeni sayı ise IntVar, kelime ise StringVar(), T/F ise BooleanVar()
x = IntVar()

check = Checkbutton(window,
                    text="Hemfikirim",
                    variable=x,             # Checbox kutucuğuna değişken atadık (İşaretleme, işaretlememe durumları)
                    onvalue=1,              # Checkbox işaretlendiğinde değişkenin alacağı değer
                    offvalue=0,             # Checkbox işaretlenmediğinde değişkenin alacağı değer
                    command=display,
                    font=("Arial", 20),
                    fg="green",
                    bg="black",
                    activeforeground="red",
                    activebackground="purple",
                    padx=25,
                    pady=10)
check.pack()

window.mainloop()