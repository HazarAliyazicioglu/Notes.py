from tkinter import *

# .move(a,x,y) a hareket ettirilicek öğe, x x ekseninde ne kadar hareket ettirileceği, y y ekseninde ne kadar hareket ettirileceği

def move_up(event):
    canvas.move(myImage,0,-10)

def move_down(event):
    canvas.move(myImage, 0, 10)

def move_left(event):
    canvas.move(myImage, -10, 0)

def move_right(event):
    canvas.move(myImage, 10, 0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

canvas = Canvas(width=500,height=500)
canvas.pack()

photoImage = PhotoImage(file="snalelogo3.png")
myImage = canvas.create_image(0,0,image=photoImage,anchor=NW)

window.mainloop()