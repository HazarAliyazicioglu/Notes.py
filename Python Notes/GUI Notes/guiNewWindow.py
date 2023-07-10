from tkinter import *

def createWindow():
    newWindow = Toplevel()  # yeni pencere diğer pencelerin üstünde açılır ve alt pencere kapanırsa TopLevel de kapanır
                # Tk() bağımsız yeni pencere açar ve alt pencere kapanırsa dahi kapanmaz
    window.destroy()  # Alt leveldeki pencereyi yeni pencere açılınca kapatır

window = Tk()

Button(window, text="create a new window", command=createWindow).pack()

window.mainloop()