# with open("x","y") y kısmına x dosyasına yazı yazmak istiyorsak w, dosyayı okutmak istiyorsak r yazarız

text = "Yoooo\nMy name is hazar\nI hope you loved this notes "

with open("Filec1.txt", "w") as file:
    file.write(text)

with open("Filec1.txt", "r") as file:
    print(file.read())


