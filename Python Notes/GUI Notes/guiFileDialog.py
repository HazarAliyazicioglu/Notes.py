from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(                          # Seçilen dosyanın ismini döndürür
        initialdir="C:\\Users\\PC\\Desktop\\Python\\Python Notes",  # Ilk klasörün açılacağı konumu belirtir
        title="Open file",                                          # Açılan klasör pencersinin başlığı
        filetypes=(("text files", "*.txt"), ("all files", "*.*")))  # Hangi tür dostaların açılabileceğini belirtir
    file = open(filepath, "r")
    print(file.read())
    file.close()


window = Tk()
button = Button(window, text="Open", command=openFile)
button.pack()
window.mainloop()