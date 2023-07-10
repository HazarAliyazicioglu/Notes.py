from tkinter import *

def drag_start(event):
    widget = event.widget                           # Herhangi bir widgette gerçekleşen eventi her widget kendi değeri olarak ayarlayabilecek
    widget.startX = event.x                         # Tıkladığımız yerdeki x koordinatını hesaplar
    widget.startY = event.y                         # Tıkladığımız yerdeki y koordinatını hesaplar

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x  # .winfo_x() bize anlık x koordinat bilgisini verir
    y = widget.winfo_y() - widget.startY + event.y  # .winfo_y() bize anlık y koordinat bilgisini verir
    widget.place(x=x,y=y)                           # Kaydırdıktan sonraki değerleri yeni koordinasyonlar olarak atarız

window = Tk()

label = Label(window,bg="red",width=10,height=5)
label.place(x=0,y=0)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)                # <B1-Motion> sol tıka basıp sürüklediğimiz anda devreye giren olay

label2 = Label(window,bg="blue",width=10,height=5)
label2.place(x=100,y=100)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()