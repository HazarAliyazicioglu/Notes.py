import math

pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))        # round(x) x ondalık sayısını en yakın sayıya yuvarlar
print(math.ceil(pi))    # math.ceil(x) x ondalık sayısını en yakın üst sayıya yuvarlar
print(math.floor(pi))   # math.floor(x) x ondalık sayısını en yakın alt sayıya yuvarlar
print(abs(pi))          # abs(x) x değerinin mutlak değerli halini döndürür
print(pow(pi, 3))       # pow(x,y) x değerini y kez kendisi ile çarpar (x^y)
print(math.sqrt(pi))    # math.sqrt(x) x değerinin karekökünü alır
print(max(x, y, z))     # max(x,y,z) x, y ve z arasından en yüksek olanı seçer
print(min(x, y, z))     # min(x,y,z) x, y ve z arasından en küçük olanı seçer