from tkinter import *

# label = Pencere içerisinde yazı veya resim barındıran widget
# https://www.tutorialspoint.com/python/tk_relief.htm relief çeşitleri için

window = Tk()

window.geometry("720x480")

photo = PhotoImage(file="snalelogo3.png")

# Pencerimize yerleştirmek istediğimiz yazıyı yazarız

label = Label(window,                       # Yerleştirileceği yer
              text="Hello World",           # Label alanına yerleştirilen yazı
              font=("Arial", 40, "bold"),   # Label içerisindeki yazı stili
              fg="green",                   # Label içerisindeki yazı rengi
              bg="black",                   # Label alanının arka planı
              relief=RAISED,                # Label alanının kenar stili
              bd=10,                        # Label alanının kenar boyutu
              padx=20,                      # Kenarla içerik arasında sağda ve solda bulunan boşluk
              pady=20,                      # Kenarla içerik arasında üstte ve aşağıda bulunan boşluk
              image=photo,                  # Label alanına yerleştirilen resim
              compound="right")             # Resimin yazının neresinde bulunacağını belirten ayar

label.pack()                                # Oluşturduğumuz yazı pencereye ekler
label.place(x=0, y=0)                       # Yazıyı pencere içerisinde pixel sistemiyle konumlandırmamızı sağlar


window.mainloop()