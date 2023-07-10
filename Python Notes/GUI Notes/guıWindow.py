from tkinter import *

# widgets = GUI elements: butons, textboxs, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()                               # Bir pencere örneğini başlatır
window.geometry("720x720")                  # Açılan pencerenin boyutunu belirler
window.title("Hazar")                       # Açılan pencerenin başlığını belirler

icon = PhotoImage(file='snalelogo3.png')    # Penceremizde icon olması için fotoğrafı dönüştürüyoruz (Dosya png olarak indirilmeli)
window.iconphoto(True, icon)                # Dönüştürdüğümüz fotoğrafı pencerenin iconu yapmamızı sağlar

window.config(background="black")           # .config() Penceremize istediğimiz özelliği eklememizi sağlar
window.mainloop()                           # Bilgisayar ekranına bir pencere açar ve istenen olayları gerçekleştirir