# reduce() = Bir iterable öğesine fonksiyon uygular ve tek bir değere kalan kadar azaltır
#            Fonksiyonu ilk iki elemnte uygular ve tek element kalana kadar devam eder
#
# reduce(function,iterable)

# reduce fonksiyonu için functoolsu import etmeliyiz
import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y: x+y, letters)
print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x*y, factorial)  # Önce 5 ve 4 sayısını çarpar çıkan sayı ile 3 sayısını ve o şekil devam eder
print(result)