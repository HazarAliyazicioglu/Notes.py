def hello():
    print("Hello")

hello()
print(hello)  # Fonksiyonun bilgisayardaki adresini gösterir

hi = hello
hi()

say = print
say("I cant believe this works")