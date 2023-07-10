# ***************************************************************************************

# https://medium.com/datarunner/pythonda-thread-i%CC%87%C5%9F-par%C3%A7ac%C4%B1%C4%9F%C4%B1-c5364ca6d8d0 threading hakkında makale

# ***************************************************************************************

# thread =  Yürütme akışı. Tıpkı birbirinden ayrı talimatlar gibi.
#           Farklı blokların içinde bulunan işçilerin (thread) birbiri ile eş zamanlı çalışması
#           Ancak, her iş parçacığı eşzamanlılık elde etmek için sırayla çalışır
#           GIL = (global interpreter lock)
#           Herhangi bir zamanda yalnızca bir iş parçacığının Python yorumlayıcısının kontrolünü elinde tutmasına izin verir

# cpu bound = program/görev, zamanının çoğunu dahili olayları bekleyerek geçirir (CPU yoğun)
#             use multiprocessing

# io bound = program/görev, zamanının çoğunu harici olayları bekleyerek geçirir (kullanıcı girişi, web kazıma)
#            use multithreading
#
# ***************************************************************************************

import threading
import time

def eat_breakfast():
    time.sleep(3)               # time.sleep(x) kodun yürütülmeden önceki x saniye kadar bekleme zamanını belirtir
    print("You eat breakfast")

def drink_milk():
    time.sleep(4)
    print("You drank milk")

def learn_python():
    time.sleep(5)
    print("You learned python")

# Aşağıda bir kod bitmeden diğeri başlayamaz
# eat_breakfast()
# drink_milk()
# learn_python()

# Bu yüzden multi-threading kullanırız. Bu fonksiyonların aynı anda çalıştırılmasını sağlar

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_milk, args=())
y.start()

z = threading.Thread(target=learn_python, args=())
z.start()

x.join()  # .join() kodu bize farklı thread modullerinin tek bir yerde toplanmasını sağlar. Bu durumda burası MainThread
y.join()
z.join()

# ***************************************************************************************

# "Kim işini bitirirse ekrana çıktıyı basıyor"
def calistir(threadname):
    for i in range(7):
        print(threadname, "çalışıyor")

t1 = threading.Thread(target=calistir, args=("thread-1", ))
t2 = threading.Thread(target=calistir, args=("thread-2", ))
t1.start()
t2.start()

# ***************************************************************************************

print(threading.active_count())  # Arka planda çalışan threading modüllerini sayar
print(threading.enumerate())     # Arka planda çalışan threading modüllerini liste olarak verir
print(time.perf_counter())       # Fonksiyonların kaç saniyede yürütüldüğünü hesaplar