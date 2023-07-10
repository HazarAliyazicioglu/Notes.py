from tkinter import *

def openFile():
    print("File has been opened!")

def saveFile():
    print("File has been saved!")

def cut():
    print("You cut some text")

def copy():
    print("You copy some text")

def paste():
    print("You paste some text")

window = Tk()

menubar = Menu(window)                                      # pencere içerisinde menubar adında menu oluşturduk
window.config(menu=menubar)                                 # Menubarımızı penceremize entegre ettik

# Ayrıca Menüler içerisinde oluşturdğumuz Komutlara fotoğrafları ekleyebilir ve compaund komutu ile hizalayabiliriz

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))   # Menubar içerisinde bulunan Filemenumuzu oluşturduk
menubar.add_cascade(label="File", menu=fileMenu)            # Filemenu menüsünü File adı ile yerleştirdik
fileMenu.add_command(label="Open", command=openFile)        # Filemenu içeriği olarak Open komutu ekledik
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()                                    # Diğer içerikler ile arasına ayırıcı koyduk
fileMenu.add_command(label="Exıt", command=quit)

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))   # tearoff menüyü açtığımzda çıkan --- işaretinin olup olmayacağını belirler
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()