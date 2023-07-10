from tkinter import *

def do(event):
    print("Mouse coordinates: " + str(event.x) + "," + str(event.y))

window = Tk()

# Tüm event durumlar için; https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
window.bind("<Button-1>",do)        # Sol tıka basıldığı an çalışır
window.bind("<Button-2>",do)        # Kaydırma tekeri kaydırıldığında çalışır
window.bind("<Button-3>",do)        # Sağ tıka basıldığı an çalışır
window.bind("<ButtonRelease>",do)   # Tıklamayı bırakma anında çalışır
window.bind("<Enter>",do)           # Pencere giriş yapma anında çalışır
window.bind("<Leave>",do)           # Pencereden çıkma anında çalışır
window.bind("<Motion>",do)          # Farenin hareket ettiği anında çalışır

window.mainloop()