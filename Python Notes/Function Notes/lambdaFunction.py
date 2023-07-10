# lambda function = Tek satırlık lambda kelimesi kullanılarak yazılmış fonksiyon
#                   Herhangi bir sayıda bağımsız değişkeni kabul eder, ancak yalnızca bir ifadeye sahiptir
#                   Kısayol olarak kullanılır ( Zaman tasarrufu )

# lamda parametre : ifade şeklinde çalışır

def double(x):
    return x*2
print(double(2))

double = lambda x: x*2  # Yukarıdaki ifadenin lamda fonksiyon hali
print(double(5))

multipy = lambda x, y: x*y
print(multipy(4, 2))

add = lambda x, y, z: x+y+z
print(add(2, 2, 2))

full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Hazar", "Aliyazıcıoğlu"))

age_check = lambda age: True if age >= 18 else False
print(age_check(19))