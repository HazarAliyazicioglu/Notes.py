full_name = "Hazar Aliyazicioglu"

print(len(full_name))               # len() değişkenimizin uzunluğunu ölçer
print(full_name.find("a"))          # .fin("x") değerimizde bulunan ilk x değerini bulur
print(full_name.capitalize())       # .capitalize() değişkenin sadece en baştaki harfini büyütür
print(full_name.upper())            # .upper() değişkenin her bir harfini büyütür
print(full_name.lower())            # .lower() değişkenin her bir harfini küçültür
print(full_name.isdigit())          # .isdigit() değişken sadece rakamlardan mı oluşuyor ona bakar
print(full_name.isalpha())          # .isalpha() değişkenimiz sadece harflerden mi oluşuyor ona bakar
print(full_name.count("a"))         # .count("x") değişkenimizdeki bütün x harflerini sayar ( Büyük küçük harf duyarlı )
print(full_name.replace("g", "ğ"))  # .replace("a", "b") değişkendeki a harfleri yerine b harfini koyar ( Büyük küçük harf duyarlı )
print(full_name*3)                  # *3 değişkenimizi 3 kez yazar