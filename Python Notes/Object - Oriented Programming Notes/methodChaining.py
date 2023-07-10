# method chaining = Birden fazla metodu aynı anda çağırmak
#                   Her biri aynı obje için çalışır ve sonucu objenin kendisine yönlendirir

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You stopped the engine")
        return self

car = Car()
car.turn_on().drive().brake().turn_off()  # Bu şekilde istediğimiz metodlarımı yada hepsini tek satırda çalıştırabiliriz

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()