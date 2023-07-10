from tkinter import *

# Scale = Kaydırma çubuğu ile ölçek oluşturma

def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")

window = Tk()

scale = Scale(window,
              from_=100,                        # Kaydırma çubuğundaki ölçüm değerlerinin başlangıç noktasını ayarlar
              to=0,                             # Kaydırma çubuğundaki ölçüm değerlerinin bitiş noktasını ayarlar
              length=600,                       # Kaydırma çubuğunun uzunluğunu ayarlar
              orient=VERTICAL,                  # Kaydırma çubuğunun dikey mi yatay mı olacağını ayarlar
              font=("Consolas", 20),
              tickinterval=10,                  # Kaydırma çubuğundaki ölçüm değerlerinin artış şeklini ayarlar
              showvalue=False,                  # Kaydırma çubuğunu kaydırırken anlık değerin gösterilme durumunu ayarlar
              resolution=1,                     # Kaydırma çubuğunun kaçar kaçar değişeceğini ayarlar
              troughcolor="blue",               # Kaydırama çubuğunun gezdiği alanın rengini ayarlar
              fg="red",                         # Yazıların rengini ayarlar
              bg="black",                       # Yazıların bulunduğu alan ve kaydırma çubuğu renklerini ayarlar
              activebackground="green")         # Kaydırma çubuğunun üstüne mouseyi götürdüğünde oluşan renk

scale.set(((scale["from"] - scale["to"]) / 2))  # Kaydrıma çubuğuna geçici değer atamamızı sağlar
scale.pack()

button = Button(window,
                text="Submit",
                command=submit)
button.pack(anchor=S)

window.mainloop()