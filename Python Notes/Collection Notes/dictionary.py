# dictionary = Değiştirilebilir, sırasız eşsiz key:değer ikilisinden oluşan koleksiyon
# Hızlılardır çünkü bizlere direkt değere ulaşma olanağı sağlar

capitals = {"ABD": "Washington DC",
            "Hindistan": "New Dehli",
            "Çin": "Beijing",
            "Rusya": "Moskova"}

capitals.update({"Almanya": "Berlin"})
capitals.pop("Çin")
# capitals.clear()

print(capitals["Almanya"])
print(capitals.get("Almanya"))  # Üstündeki kod ile aynı işlemi yapar
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key, value)