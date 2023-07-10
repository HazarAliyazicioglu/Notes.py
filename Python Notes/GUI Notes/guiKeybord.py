from tkinter import *

def doSomething(event):
    print("You pressed: " + event.keysym) # event.keysym bind metodundaki eylemde kullanılan tuşun sembolünü verir
    label.config(text=event.keysym)
window = Tk()

# .bind(event,function) şeklinde çalışır ve event kısmında bahsedilen eylem yapıldığında fonksiyon çağırır
# Tüm event çeşitleri için https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
window.bind("<Key>",doSomething)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()