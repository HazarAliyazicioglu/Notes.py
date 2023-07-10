from tkinter import  *
from tkinter import filedialog

def save():
    file = filedialog.asksaveasfile(defaultextension=".txt",    # Dosyanın varsayılan kaydetme uzantısını belirler
                                    filetypes=[                 # Dosyanın hangi türde kaydedileceğini belirtir
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All file", ".*")
                                   ])
    if file is None:
        return
    filetext = str(text.get("1.0", END))
    # filetext = input("Enter some text I guess: ") // Eğer konsolu kullanarak dosyaya birşeyler yazıp kaydetmek isterseniz
    file.write(filetext)
    file.close()

window = Tk()
save = Button(window, text="Save", command=save)
save.pack()
text = Text(window)
text.pack()
window.mainloop()