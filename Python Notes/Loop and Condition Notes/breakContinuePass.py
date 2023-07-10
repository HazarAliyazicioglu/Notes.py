# Loop Control Statements = Döngünün işleyişini değiştirmemizi sağlayan ifadeler

while True:
    name = input("Enter your name:")
    if name != "" and name != " ":
        break
print("Hello "+name)

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)