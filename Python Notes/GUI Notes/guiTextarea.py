from tkinter import *

def submit():
    inbut = text.get("1.0", END)
    print(inbut)

window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Segoe Print", 60),
            height=4,
            width=10,
            padx=20,
            pady=20,
            fg="red")
text.pack()

submit = Button(window, text="Submit", command=submit)
submit.pack()

window.mainloop()