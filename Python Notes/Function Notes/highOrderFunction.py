# High Order Functions = 2 farklı görevi yapabilen fonksiyonlar
#                        1) Başka bir fonksiyonu argüman olarak kabul etmek
#                        2) Fonksiyon döndürmek
#                        ( Python dilinde fonksiyonlar aynı zamanda objedir )

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(quiet)
hello(loud)


# divisor = bölen, dividend = bölünen, quotient = sonuç
def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)     # Fonksiyonu değişkene atayarak x bilinmeyenine değer atıyoruz atadığımız x değeri belleğe yerleşiyor
print(divide(10))       # Değişkeni fonksiyon şeklinde yazarak bir değer veriyoruz bu seferde y değişkenini atamış oluyoruz