from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)              # Canvas alanı oluşturduk sol en üst köşe 0,0 iken sağ en alt köşe ise 500,500'dür

canvas.create_line(0,0,500,500,fill="blue",width=5)         # x0,y0 ve x1,y1 noktaları arasında çizgi oluşturur fill ikle renk ayarı veririz
canvas.create_line(0,500,500,0,fill="red",width=5)

canvas.create_rectangle(50,50,250,250,fill="purple")        # x0,y0 x1,y2 noktalarını birleştirerek dikdörtgen oluşturur

points = [250,0,500,500,0,500]                              # Başka bir öğe yaratmak için koordinat noktaları belirleriz

canvas.create_polygon(points,fill="yellow",outline="black") # x0,y0 x1,y2 x3,y3 noktalarını birleştirerek çokgen oluşturur

canvas.create_arc(500,500,0,0,fill="white",extent=180,start=180,width=10)
# Dairesel alan oluşturur
# extend alanın derecesini, start hangi derceden başlıyacağını, width = alanın dış çizgi genişliğini ayrlar

canvas.create_oval(190,190,310,310,fill="white",width=10)
# Oval oluşturur
# x0,y0 x1,y1 noktalarını seçer ve böylelikle konumunu belirleriz

canvas.pack()

window.mainloop()