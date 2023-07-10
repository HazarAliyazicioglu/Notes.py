import random               # Random modullerine erişim sağlamak için yazarız

x = random.randint(1, 6)    # .randint(x, y) x ile y arasında bir sayı üretir
y = random.random()         # .random() 0 ile 1 arasında bir sayı üretir

myList = ["rock", "paper", "scissors"]
z = random.choice(myList)   # .choice(x) erişimi olan x koleksiyonundan rastgele öğe seçer

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]

random.shuffle(cards)       # .shuffle(x) erişimi olan x koleksiyonunu rastgele karıştırır

print(x)
print(y)
print(z)
print(cards)