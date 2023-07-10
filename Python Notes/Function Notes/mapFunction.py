# map() = İterable içerisindeki bütün itemlere fonksiyon uygular
#
# map(function, iterable) şeklinde çalışır

store = [("shirt", 10.00),
         ("pants", 15.00),
         ("pants", 20.00),
         ("jackets", 5.00)]

to_turkishLira = lambda data: (data[0], data[1]*26.07)

store_turkishLİra = list(map(to_turkishLira, store))
for i in store_turkishLİra:
    print(i)