class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):  # Ebeveyn classında bulunan metodu çocuk classta değiştirdik
        print("This rabbit eating a carrot")

class Hawk(Animal):
    pass

rabbit = Rabbit()
hawk = Hawk()

rabbit.eat()
hawk.eat()