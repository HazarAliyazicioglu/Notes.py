from tkinter import *
from tkinter.ttk import *
import time

def download():
    GB = 100
    downloaded = 0
    speed = 1
    while(downloaded<GB):
        time.sleep(0.05)
        bar['value'] += (speed/GB)*100
        downloaded += speed
        percent.set(str(int((downloaded/GB)*100))+"%")
        text.set(str(downloaded)+"/"+str(GB)+" GB completed")
        window.update_idletasks()

window = Tk()
window.geometry("720x220")
percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=250)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
textLabel = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=download).pack()

window.mainloop()