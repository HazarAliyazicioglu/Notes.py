# zip (*iterables) = İki yada daha fazla dizinden elementler kümeleştirir
#                    Her öğe için dizinlerde depolanan eşleştirilmiş öğelerle bir zip nesnesi oluşturur

usernames = ["Hazar", "Nasuh", "Eren"]
passwords = ["2040", "22Barney", "1Yoda1"]
login = ["10/10/2001", "11/07/2001", "18/02/2001"]

users = zip(usernames, passwords)
print(type(users))
for i in users:
    print(i)

users = list(zip(usernames, passwords))
print(type(users))
for i in users:
    print(i)

users = dict(zip(usernames, passwords))
print(type(users))
for key,value in users.items():
    print(key + ":" + value)

users = zip(usernames, passwords,login)
print(type(users))
for i in users:
    print(i)