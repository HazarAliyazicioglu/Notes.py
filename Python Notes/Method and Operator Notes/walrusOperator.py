# walrus operator :=
# daha büyük ifadenin bir parçası olarak değişkenlere değerler atar

tired = True
print(tired)

print(tired := True)

foods = list()

""""

while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    else:
        foods.append(food)

"""

while food := input("What food do you like?: ") != "quit":
    foods.append(food)

# Satır sayısını azaltmayı amaçlar örneğin yukarda if else bloğu kullanarak normalde 6 satırda yapılan kodu 2 koda düşürdü
