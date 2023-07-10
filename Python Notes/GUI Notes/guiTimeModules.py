from tkinter import *
from time import *

# Time modülleri için: https://www.programiz.com/python-programming/time

def update():
    timeString = strftime("%I:%M:%S %p")        # strftime() metodu ile modülleri kullanarak gerçek zamanlı tarih ve zaman değerlerini elde edebiliriz
    timeLabel.config(text=timeString)

    dayString = strftime("I love you on %A")
    dayLabel.config(text=dayString)

    dateString = strftime("%B %d, %Y")
    dateLabel.config(text=dateString)

    window.after(1000,update)                   # .after() metodu ile her 1000 milisaniyede bir yenileniyor

window = Tk()

window.title("Love Clock")

timeLabel = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
timeLabel.pack()

dayLabel = Label(window,font=("Ink Free",25))
dayLabel.pack()

dateLabel = Label(window,font=("Ink Free",30))
dateLabel.pack()

update()

window.mainloop()

