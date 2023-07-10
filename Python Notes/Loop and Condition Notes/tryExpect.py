
# expect = Prgramın çalışması sırasında programın akışını bozan şeyleri bulmak

# The try block: lets you test a block of code for errors.
# The except block: lets you handle the error.
# The else block: lets you execute code when there is no error.
# The finally block: lets you execute code, regardless of the result of the try- and except blocks.

try:
    numerator = int(input("Bölünecek sayıyı yazınız:"))
    denominator = int(input("Bölen sayıyı yazınız:"))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("0 ile hiçbir sayı bölünmez seni salak")
except ValueError as e:
    print(e)
    print("Lütfen sadece sayı giriniz")
except Exception as e:
    print(e)
    print("Küçük bir sıkıntı yaşandı")
else:
    print(result)
finally:
    print("Bu kısım her zaman çalışacak")

