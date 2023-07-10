import os

source = "Filec1.txt"                                                       # Hareket ettirmek istediğimiz dosya
destination = "C:\\Users\\PC\\Desktop\\Python\\Python Notes\\Filec2.txt"    # Hareket ettireceğimiz yer

try:
    if os.path.exists(destination):
        print("There is already a file")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")