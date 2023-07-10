# nested functions = İç içe geçmiş fonksiyonların birbirini çağırması ile oluşur
#                    bir fonksiyondan çıkan değer diğer fonksiyonun argümanı olur

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

print(round(abs(float(num))))  # Üstündeki kod bloğunun tek satırda toplanmış hali