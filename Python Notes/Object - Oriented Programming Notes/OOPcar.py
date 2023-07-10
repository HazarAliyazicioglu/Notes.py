class Car:

    wheels = 4  # class variable ( oluşturulan her objede aynı olan değişkenler )

    # Nesne oluşturduğumuz zaman nesnenin değerlerini vermek için constructor oluştururuz
    # self oluşturduğumuz nesnenin constructor içerisindeki niteliklere erişmesini sağlar

    def __init__(self, make, model, year, color):  # __init__ class içerisinde yapıcı (constructor) methodları oluşturmak için kullanılır
        self.make = make    # instance variable
        self.model = model  # instance variable
        self.year = year    # instance variable
        self.color = color  # instance variable  ( oluşturulan objelere göre değişkenlik gösterilebilen değişkenler )

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")