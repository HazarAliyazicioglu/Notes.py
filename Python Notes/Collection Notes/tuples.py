# tuple = Sıralı ve değiştirilemeyen koleksiyonlar

student = ("Hazar", 22, "Male")
print(student.count("Hazar"))   # .count(x) bize koleksiyondaki x değerinin sayısını verir
print(student.index("Male"))    # .index(x) bize koleksiyondaki x değerinin sırasını verir

for x in student:
    print(x)

if "Hazar" in student:
    print(student[0] + " is here!")

if "hazar" in student:
    print(student[0] + " is here!")  # Yürütülemez çünkü büyük küçük harf duyarlılığından koşul gerçekleşemez