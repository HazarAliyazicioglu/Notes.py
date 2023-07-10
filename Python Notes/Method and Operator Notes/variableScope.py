# scope = Değişkenin tanımlandığı bölge
#         Değişken sadece yaratıldığı bölge içerisinde geçerlidir
#         Global ve local scope olmak üzere ikiye ayrılır

name = "Hazar"      # Global Scope ( Fonksiyonların içinde de dışında da kullanılabilir )

def display_name():
    name = "Code"   # Local Scope ( Sadece oluşturulduğu fonksiyonda geçerlidir )
    print(name)

display_name()
print(name)