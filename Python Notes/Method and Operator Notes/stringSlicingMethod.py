# slicing = String bir değerden başka bir string değeri oluşturmak
# indexing[} yada slice()
# [start, stop, step]

name = "Hazar Aliyazıcıoğlu"

first_name = name[:5]       # [0:3]
last_name = name[6:]        # [6:end]
funky_name = name[::2]      # [0:end:2] 0'dan başlayıp 2'şer 2'şer yana gidiyor
reversed_name = name[::-1]  # [0:end:-1] başlangıç yerini yazmadığımız için bütün metni tersine çevirir

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slicey = slice(7, -4)  # Baştan 7. sıradan en sondan 4. sıraya kadarki olan kısmı keser ( Tersten gelirken saymaya 0'dan başlanmaz )
print(website1[slicey])
print(website2[slicey])