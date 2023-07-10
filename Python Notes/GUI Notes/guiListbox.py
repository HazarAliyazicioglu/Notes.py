# listbox = Seçilebilen öğeleri listeleyen alan

from tkinter import *

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You ordered")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entry.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):      # .curselection() seçilen öğeyi ifade eder
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE,                  # Listeden öğe seçme ayarı
                  selectbackground="red",               # Seçilen öğelerin arka plan rengi ayarı
                  selectforeground="green")             # Seçilen öğelerin yazı rengi ayarı
listbox.pack()

listbox.insert(1, "Köfte")                              # Öğelerin indexi (sırası) ve ismi
listbox.insert(2, "Güveç")
listbox.insert(3, "Lahmacun")
listbox.insert(4, "İskender")
listbox.insert(5, "Pirzola")
listbox.config(height=listbox.size())

entry = Entry(window)
entry.pack()

submit = Button(window, text="Submit", command=submit)
submit.pack()

add = Button(window, text="Add", command=add)
add.pack()

delete = Button(window, text="Delete", command=delete)
delete.pack()


window.mainloop()