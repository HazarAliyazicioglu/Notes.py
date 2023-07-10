# inherit = Ebeveynden çocuğuna geçen dna, kalıtım

class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):   # Parantez içerisinde yazdığımız yer Rabbit classının Ebeveyn classı oluyor
    pass

class Fish(Animal):     # Ebeveyn classta bulunan tüm özellikler çocuk classlara da aktarılıyor
    pass

class Hawk(Animal):     # Ayrıca istersek çocuk classa farklı özellikler verebiliriz
    def fly(self):
        print("Hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
hawk.fly()