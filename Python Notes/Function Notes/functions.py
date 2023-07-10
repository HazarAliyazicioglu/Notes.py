# function = Sadece çağırıldığında yürütülen kod bloğu

def hello(first_name, last_name, age):
    print("Hello " + first_name + " " + last_name)
    print("You are " + str(age) + " years old")
    print("Have nice day")

hello("Hazar", "Aliyazıcıoğlu", 22)

name = "Hazar"
lastname = "Aliyazıcıoğlu"
myAge = 22

hello(name, lastname, myAge)