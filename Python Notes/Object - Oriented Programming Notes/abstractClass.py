# Nesne oluşturulmasını önler
# Çocuk classı ebeveynde bulunan abstract methodları geçersiz kılmaya zorlar (override yapmaya yani yeni method oluşturmaya)

# abstract class = bir yada daha fazla abstract methodu barındıran classlar
# abstract method = bir açıklaması olan ama uygulaması olmayan methodlar

from abc import ABC, abstractmethod  # abstract kullanabilmek için import ediyoruz
# abc = abstract based class
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride motorcycle")

# vehicle = Vehicle() objesini oluşturamayız çünkü ebeveyn classta abstract method çalışmaktadır
car = Car()
motor = Motorcycle()

# vehicle.go()
car.go()
motor.go()