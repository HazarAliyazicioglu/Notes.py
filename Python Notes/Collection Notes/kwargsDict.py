# **kwargs = Bütün argümanları dictionarye toplayan parametre
#            Bir fonksiyonun farklı sayılarda anahtar kelimeyi barındırabilmesi açısından kullanışlıdır

def hello(**kwargs):
    print("Hello " + kwargs["first"] + " " +kwargs["last"])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(title="Mr.", first="Hazar", middle="Dude", last="Code")