from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)     # Bir pencere koleksiyonunu yöneten widget öğesi oluşturuyoruz

tab1 = Frame(notebook)              # Tab1 sekmesi için yeni bir çerçeve yaratıyoruz
tab2 = Frame(notebook)              # Tab2 sekmesi için yeni bir çerçeve yaratıyoruz

notebook.add(tab1, text="Tab 1")    # Yarattığımız sekme çerçevelerini widget öğemize ekliyoruz
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")     # expand ayarı kullanılmayan herhangi bir alanı doldurma görevi görür
                                            # fill ayarı dikey ve yatay eksendeki boşlukları doldurur

Label(tab1, text="This is tab1", width=50, height=25).pack()    # Tab1 sekmemizin içine 50 genişlik 25 yüksekliğe ait yazı ekliyoruz
Label(tab2, text="This is tab2", width=50, height=25).pack()

window.mainloop()