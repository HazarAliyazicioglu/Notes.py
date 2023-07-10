# nested loops = İç içe geçmiş birden fazla döngülerden oluşur

rows = int(input("How many rows?:"))
columns = int(input("How many columns?:"))
symbol = input("Enter a symbol to use:")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")  # end="" Parantez içine koyulan öğeyi kendisinden önce gelen değişkenenin sonuna ekler
    print()