from tkinter import *

# button = Tıkladığında etkileşim aldığın öğe

count = 0

def click():
    global count  # Global değişken olarak atarız böylece heryerde değişkene erişebiliriz
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file="snalelogo3.png")

button = Button(window,                             # Yerleştirileceği yer
                text="Click",                       # Label alanına yerleştirilen yazı
                command=click,                      # Tıklandığında işleme giricek komut
                font=("Comic Sans", 30, "italic"),  # Button yazı stili
                fg="#00FF00",                       # Button yazı rengi
                bg="black",                         # Button arka planı
                activeforeground="#00FF00",         # Buttona tıkladığında yazının rengi
                activebackground="black",           # Buttona tıkladığında arka planın rengi
                state=ACTIVE,                       # Buttonun tıklanabilir mi tıklanamaz mı olduğunu ayarlar
                image=photo,                        # Butonun içine koyulan resim
                compound="right"                    # Buttonun içindeki resmin yazının neresinde bulunacağını belirtir
                )
button.pack()

window.mainloop()