from tkinter import *

# entry widget = Kullanıcıların bir satırlık kelime girebildikleri alan

def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(window,
              font=("Sans Serif", 20),
              fg="#00FF00",
              bg="black",
              show="*")         # ENtrye girilen değerleri * olarak gösterir

entry.insert(10, "Spongebob")   # Entry boxun içerisine bir placeholder ("Username:" gibi) yerleştirmemizi sağlar
entry.pack(side=LEFT)

submit = Button(window, text="Submit", command=submit)
submit.pack(side=RIGHT)

delete = Button(window, text="Delete", command=delete)
delete.pack(side=RIGHT)

backspace = Button(window, text="Backspace", command=backspace)
backspace.pack(side=RIGHT)

window.mainloop()