from tkinter import *
from time import *

# Time modülleri için: https://www.programiz.com/python-programming/time

def update():
    timeString = strftime("%I:%M:%S %p")
    timeLabel.config(text=timeString)

    dayString = strftime("%A")
    dayLabel.config(text=dayString)

    dateString = strftime("%B %d, %Y")
    dateLabel.config(text=dateString)

    window.after(1000,update)

window = Tk()

window.title("Clock")

timeLabel = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
timeLabel.pack()

dayLabel = Label(window,font=("Ink Free",25))
dayLabel.pack()

dateLabel = Label(window,font=("Ink Free",30))
dateLabel.pack()

update()

window.mainloop()

