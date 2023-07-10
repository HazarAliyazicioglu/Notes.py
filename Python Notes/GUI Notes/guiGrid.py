from tkinter import *

# grid() = Geometri yöneticisi, Widgetlerin alanlarını istediği şekilde yönetir
# grid() içersiinde bulunan row satırı x eksenini, column sütunu y eksenini belli eder
# columnspan bir öğenin kaç tane sütunluk alan kapsadığını söyler
# rowspan bir öğenin kaç tane satırlık alan kapsadığını söyler

window = Tk()

firstNameLabel = Label(window, text="First name: ").grid(row=0, column=0)
firstNameEntry = Entry(window).grid(row=0, column=1)

lastNameLabel = Label(window, text="Last name: ").grid(row=1, column=0)
lastNameEntry = Entry(window).grid(row=1, column=1)

emailLabel = Label(window, text="E-mail: ").grid(row=2, column=0, columnspan=1)
emailEntry = Entry(window).grid(row=2, column=1)

submit = Button(window, text="Submit").grid(row=3, column=0, columnspan=2)

window.mainloop()