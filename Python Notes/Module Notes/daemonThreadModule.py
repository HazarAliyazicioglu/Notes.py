# daemon thread = Arka planda çalışan bir thread, programın çalışması için önemli değil
#                 Program bitmek için daemon threadlerin çalışmasını beklemez
#                 daemon olmayanlar görev tamamlanana kadar devam ederler

import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: " + str(count) + " seconds")

# daemon = True dersek threadimiz sonsuza kadar sürmesi gerekse bile diğer treadler bittiği zaman kendisi de sonlanır
x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon() başka bir thread modulünde threadi daemon yapmak için kullanılır
# print(x.isDaemon()) başka bir thread modulünde threadin daemon olup olmadığını kontrol eder

answer = input("Do you wish to exit ? ")