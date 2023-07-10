
#  Eğer dosya bu dosya ile aynı konumda değilde başka yerde olsaydı o zaman adresini yazmamız gerekirdi
#  Örneğin dosya masaüstünde olsaydı with open("C:\\Users\\PC\\Desktop\\Filec1.txt") şeklinde olacaktı

try:
    with open("Filec1.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("Dosya bulunamadı!")
except FileExistsError:
    print("Dosya bulundu")
else:
    print("Sıkıntı yok")
finally:
    print("İşlem tamamlandı")