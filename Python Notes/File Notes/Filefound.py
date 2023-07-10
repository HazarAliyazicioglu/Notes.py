import os

path = "/Python Notes/Filec1.txt"  # Eğer bir tane ters eğik çizgi var ise string olmaması için bir tane daha koyarız
                                                                   # Eğer en sondaki bir klasör olsaydı isdir() metodunda geçen kısım çalışacaktı

if os.path.exists(path):
    print("Aradığınız konum bulunmakta")
    if os.path.isfile(path):
        print("Bu bir dosyadır")
    elif os.path.isdir(path):
        print("Bu bir klasördür")
    else:
        print("Bu ne?")
else:
    print("Aradığınız konum bulunmamakta")
