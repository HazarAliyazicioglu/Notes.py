# str.format() = Kullanıcıların çıktıyı görüntülerken daha çok kontrolleri olması için bir metod
#                Parantez "" içinde bulunan {} yerine koymak istediğimizde cümle sonuna.format(x) ekleriz

animal = "Dog"
item = "steak"
print("{} loves {}".format("Dog", "steak"))
print("{} loves {}".format(animal, item))
print("{1} loves {0}".format(animal, item))
print("{animal} loves {item}".format(animal="Cat", item="milk"))
text = "{} loves {}"
print(text.format(animal, item))

name = "Hazar"
print("Hello my name is {}".format(name))
print("Hello my name is {:10}. Nice to meet you!".format(name))     # formatı yerleştireceğimiz yere kelimeden sonra 10 harflik boşluk açar
print("Hello my name is {:<10}. Nice to meet you!".format(name))    # formatı en sağa yerleştirerek 10 kelimelik boşluk açar
print("Hello my name is {:>10}. Nice to meet you!".format(name))    # formatı en sola yerleştirerek 10 kelimelik boşluk açar
print("Hello my name is {:^10}. Nice to meet you!".format(name))    # formatı ortaya yerleştirerek 10 kelimelik boşluk açar


number = 1000

print("The number is {:.3f}".format(number))    # Formata yerleştirilen değeri ondalıklı yapar ve ondalıklı kısmı 3 haneden oluşur
print("The number is {:,}".format(number))      # Her binlikte bir virgül koyar
print("The number is {:b}".format(number))      # Sayımızı binar ( ikilik ) sisteme çevirir
print("The number is {:o}".format(number))      # Sayımızı octal ( sekizlik ) sisteme çevirir
print("The number is {:X}".format(number))      # Sayımızı hexadecimal ( onaltılık ) sisteme çevirir ( Küçük x hexadecimaldeki harfleri küçük yazar )
print("The number is {:E}".format(number))      # Sayımızı bilimsel sisteme çevirir ( Küçük e bilimseldeki harfleri küçük yazar )