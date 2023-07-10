from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered hamburger")
    elif x.get() == 2:
        print("You ordered hotdog")
    else:
        print("Huh?")

window = Tk()

x = IntVar()


for index in range(len(food)):
    radio = Radiobutton(window,
                        text=food[index],
                        variable=x,         # Aynı değeri taşıyan bütün radio buttonları birleştirir
                        value=index,        # Her bir radio buttonuna farklı değer atar
                        padx=25,
                        font=("Impact", 50),
                        indicatoron=False,  # Yuvarlak göstergeleri kaldırır
                        width=375,          # Radio buttonların genişlik ayarı
                        command=order)

    # anchor bize öğenin düzenlenme şeklini söyler
    # N = Kuzey, S = Güney, W = Batı, E = Doğu , CENTER = Merkez, diğer yönlerin birleşimleri NW gibi
    radio.pack(anchor=W)

window.mainloop()
