# for döngüsü =  Belli bir aralıkta yürütülen döngü

import time

for i in range(10):
    print(i+1)

for i in range(50, 100+1, 2):       # range( start,end,steps ) 50den 101e 2şer 2şer
    print(i)

for i in "Hazar":
    print(i)

for seconds in range(10, 0, -1):    # range( start,end,steps ) 10dan 0a geriye doğru
    print(seconds)
    time.sleep(1)                   # time.sleep(x) kodun x süre kadar durdurulmasını sağlar
print("Happy New Year!")