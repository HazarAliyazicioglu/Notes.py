# list comprehension = Daha az öğe ile yeni bir liste oluşturmanın yolu
#                      Belirli lambda fonksiyonlarını taklit edebilir, okunması daha kolay
# list comprehension kullanımı                      list = [ expression, for item, in iterable ]
# Bir koşul ve bir sonuç olduğunda                  list = [ expression, for item, in iterable if condition ]
# Birden fazla koşul ve sonuç olduğu durumlarda     list = [ expression, (if/else), for item, in iterable ]

squares = []                # Boş bir liste oluşturduk
for i in range(1, 11):      # Döngü oluşturduk
    squares.append(i * i)   # Döngünün her bir adımında neler yapacağını yazdık
print(squares)


squares = [i * i for i in range(1, 11)]
print(squares)
# expression = i*i
# for item = for i
# in iterable = in range(1,11)

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
# passed_students = list(filter(lambda x: x >= 60, students))
passed_students1 = [i for i in students if i >= 60]
passed_students2 = [i if i >= 60 else "Failed" for i in students ]
print(passed_students1)
print(passed_students2)