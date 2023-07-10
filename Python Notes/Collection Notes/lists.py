# list = Birden fazla itemi tek bir değişkende depolamamızı sağlar

food = ["hamburger", "karniyarik", "pizza", "pudding", "hotdog"]

print(food[1])

food[0] = "sushi"           # listedeki 0. elemana değer atamamızı sağlar

food.append("ice cream")    # .append("x") listenin sonuna x elemanını ekler
food.remove("hotdog")       # .remove("x") listeden x elemanını çıkarır
food.pop()                  # .pop() listenin son elemanını siler
food.insert(0, "cake")      # .insert(a, "x") listenin a. sırasına x elemanını ekler
food.sort()                 # .sort() listeyi alfabetik olarak sıralar
food.clear()                # .clear() listenin tüm elemanlarını yok eder

for x in food:
    print(x)
