from tkinter import *
import time

WIDTH = 750
HEIGHT = 750
xVelocity = 3               # x eksenindeki hız değerimiz
yVelocity = 2               # y eksenindeki hız değerimiz

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

photo = PhotoImage(file="ufo.png")
my_image = canvas.create_image(0,0,image=photo,anchor=NW)   # Canvas fotoğrafı oluşturduk (x,y,içerik,konumlandırılma yeri)

image_width = photo.width()
image_height = photo.height()

while True:
    coordinates = canvas.coords(my_image)                   # .coords() bize canvas öğesinin x ve y koordinatlarını verir
    print(coordinates)
    if coordinates[0] >= (WIDTH-image_width) or coordinates[0] < 0:
        xVelocity = -xVelocity
    if coordinates[1] >= (HEIGHT-image_height) or coordinates[1] < 0:
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)               # .move(hareket etmesini istediğimiz öğe, x hızı, y hızı)
    window.update()
    time.sleep(0.01)

window.mainloop()