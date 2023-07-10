# Değişken = herhangi bir değeri belirtmek için atanılan içerik
# int = integer, Tam sayıları ifade eder
# str = string Kelimeleri ifade etmek için kullanılır
# float = float Ondalıklı sayılar için kullanılır
# boolean Doğru yada yanlış ifadeleri için kullanılır

name = "Hazar"
print(type(name))

lastname = "Aliyazicioglu"
print(lastname)

print(name + " " + lastname)

age = 21
print(age)
print("My age is " + str(age))              # string bir ifadenin sonuna integer bir ifade konulamaz

height = 1.80
print(type(height))
print("My height is " + str(height))        # string bir ifadenin sonuna float bir ifade konulamaz

dog = False
cat = False
brother = True
print(type(dog))
print(brother)
print("Do you have any dogs? " + str(cat))  # string bir ifadenin sonuna boolean   bir ifade konulamaz


# Çoklu Atama = Tek bir satır içerisinde birden fazla kez atama yapmamızı sağlar
name, age, attractive = "Hazar", 22, True
print(name)
print(age)
print(attractive)

# Birden fazla değişken aynı değer alıyor ise
Kratos = Fortesque = ArthurMorgan = Dante = "Game Character"

print(Kratos)
print(Fortesque)
print(ArthurMorgan)
print(Dante)