from tkinter import *
import time
from guiMultipleAnimationsBall import *
window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg="purple")
canvas.pack()

voleyball = Ball(canvas,0,0,100,1,1,"blue")     # oluşturduğumuz nesne dosyasındaki değişkenlere değer atadık
baseball = Ball(canvas,100,100,150,2,3,"red")
football = Ball(canvas,300,300,350,4,3,"black")

while True:
    voleyball.move()                            # .move() metodu canvasları hareket ettirmemizi sağlar
    baseball.move()
    football.move()
    window.update()
    time.sleep(0.01)

window.mainloop()