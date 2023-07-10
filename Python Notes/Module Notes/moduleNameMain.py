# *************************
# if __name__ == "__main__"
# *************************

# İfade bize kodumuzun başka bir dosyadan mı yoksa değrudan mı çalıştırıldığını gösterir
# __name__ dosya doğrudan çalıştırıldığında __main__ değerini alır
# Ancak import edilen bir dosya tarafından gerçekleşirse __name__ değeri o dosyanın adını alır

# Modüller bağımsız programlar olarak yürütülebilir
# Modüller başka modüller tarafından import edilip kullanılabilir

# Python tercüman setleri "special variables", bunlardan biri __name__

if __name__ == "__main__":
    print("Doğrudan çalıştırıldı")
else:
    print("Başka dosyadan çalıştırıldı")