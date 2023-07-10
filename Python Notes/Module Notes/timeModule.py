# Time modülleri için https://docs.python.org/3/library/time.html

import time

# epoch = Bilgisayarınızın çağ/devirin ne zaman başladığına dair sahip olduğu düşünce

# .ctime(x) epochdan sonrasına x kadar saniyeler ekleyerek okunabilir bir stringe dönüştürür
# .time() epochtan bu yana geçen saniyeleri gösterir
# .localtime() bize bulunduğumuz ana kadar geçen zamanı ve tarihi struct halinde gösterir
# .gmtime() evrensel bilgiler ile bulunduğun saati ve tarihi gösterir
# .strptime() seçilen anahtarlara göre değikenin struct halini verir (localtime gibi)
# .asctime() girilen değerlere göre struct halden stringe tarih ve saat olarak döndürür
# .mktime() girilen değerlere göre epochtan sonra geçen zamanı saniye bilgisi olarak verir

print(time.ctime(1))
print(time.time())
print(time.ctime(time.time()))  # Günümüz tarihini ve saatini gösterir

time_object = time.localtime()
time_object = time.gmtime()
print(time_object)
print(time.strftime("%B %d %Y %H:%M:%S", time_object))

time_string = "10 October, 2001"
print(time.strptime(time_string, "%d %B, %Y"))

# ( year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst )
time_tuple = (2022, 5, 12, 21, 31, 14, 2, 0, 0)
print(time.asctime(time_tuple))

# ( year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst )
time_tuple = (2022, 5, 12, 21, 31, 14, 2, 0, 0)
print(time.mktime(time_tuple))