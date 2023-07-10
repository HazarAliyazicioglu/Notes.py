# filter() = bir fonksiyonun döndürdüğü bir iterableden öğeler koleksiyonu oluşturur
#
# filter(functions,iterable)

friends = [("Rachel", 19),
         ("Monica", 16),
         ("Phoebe", 17),
         ("Joey", 18),
         ("Chandler", 21),
         ("Ross", 20)]

age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))
sorted_drinking_buddies = sorted(drinking_buddies)

for i in sorted_drinking_buddies:
    print(i)