
# https://builtin.com/data-science/copy-a-file-with-python about copy system

# copyfile() =  Dosyanın içeriğini kopyalar
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata ( File's creation and modification times )

import shutil

shutil.copy2("Filec1.txt", "Filec2.txt")
# shutil.copyfile("Filec1.txt", "Filec2.txt")
# shutil.copy("Filec1.txt", "C:\\Users\\PC\\Desktop\\Python\\Python Notes\\Filec2.txt" )

with open("Filec2.txt") as file:
    print(file.read())
