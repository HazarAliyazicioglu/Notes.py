# Duck typing = Bir obje classının herhangi bir methodtan yada nitelikten daha az öenmli olduğu konsept
#               Minimum yöntemler veya nitelikler mevcutsa sınıf türü kontrol edilmez
#               "Eğer ördek gibi yürüyor ve ördek gibi ses çıkarıyorsa o zaman o bir ördektir"

class Duck:
    def walk(self):
        print("Duck is walking")

    def talk(self):
        print("Duck is quacking")

class Chicken:
    def walk(self):
        print("Chicken is walking")

    def talk(self):
        print("Chicken is clucking")

class Person:
    def catch(self, duck):
        duck.talk()
        duck.walk()
        print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)

# https://towardsdatascience.com/duck-typing-python-7aeac97e11f8 konu hakkında bir makale

