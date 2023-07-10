# logical operators ( and,or,not ) = Birden fazla koşul durumu olduığunda kullanılır

temp = int(input("What is temperature outside?"))

if temp >= 0 and temp <= 30:
    print("Temperature is good")
    print("Go outside")
elif temp < 0 or temp >30:
    print("Temperature is bad today")
    print("Stay inside")

sick = input("Are u ok?")

if sick == "yes":
    print("You can go outside")
elif not sick == "yes":
    print("Rest in house")