class Car:
    color = None

class Motorcycle:
    color = None
def change_color(car, color):
    car.color = color

car1 = Car()
car2 = Car()
car3 = Car()
bike1 = Motorcycle()

change_color(bike1, "green")
change_color(car1, "red")
change_color(car2, "black")
change_color(car3, "blue")

print(car1.color)
print(car2.color)
print(car3.color)
print(bike1.color)