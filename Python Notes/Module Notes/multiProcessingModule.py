# multiprocessing = Farklı CPU çekirdeklerinde paralel şekilde yürütülen işlemler
#                   multiprocessing = İŞlemciye bağlı işlemler için daha iyi (Yüksek CPU kullanımı)
#                   multithreading = İnput/outputa bağlı işlemlerde daha iyi (Zaman öldürmek)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    print(cpu_count())  # Sistemdeki Cpu sayısına göre aynı anda kaç işlem yapabileceğini hesaplar

    a = Process(target=counter, args=(100000000,))
    a.start()
    a.join()

    b = Process(target=counter, args=(100000000,))
    b.start()
    b.join()

    c = Process(target=counter, args=(100000000,))
    c.start()
    c.join()

    d = Process(target=counter, args=(100000000,))
    d.start()
    d.join()

    e = Process(target=counter, args=(100000000,))
    e.start()
    e.join()

    f = Process(target=counter, args=(100000000,))
    f.start()
    f.join()

    g = Process(target=counter, args=(100000000,))
    g.start()
    g.join()

    h = Process(target=counter, args=(100000000,))
    h.start()
    h.join()

    print("Finished in:", time.perf_counter(), "seconds")

main()