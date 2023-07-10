# Nesne Tabanlı Programlama

from OOPcar import Car

car_1 = Car("Chevy", "Corvette", 1979, "Black")
car_2 = Car("Bugatti", "Veyron", "2010", "Blue")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_2.stop()