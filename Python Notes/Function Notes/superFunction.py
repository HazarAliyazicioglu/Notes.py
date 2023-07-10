# super() = Ebeveyn classının metodlarına erişmemizi sağlayan fonksiyon
#           Kullanıldığı zaman ebeveyn classın geçici bir değerini döndürür
#           Örneğin aşağıda tekrar tekrar self.x yazmak yerine ebeveyn classta yazarız ve daha sonra super fonksiyon ile tekrar metodları çağırmış oluruz

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())