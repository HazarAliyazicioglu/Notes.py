# *args = Bütün argümanları tek bir tuple içine sığdıran parametre
#         Bir fonksiyonun farklı sayılarda değişkeni barındırabilmesi açısından kullanışlıdır

def add(*nums):
    sum = 0
    nums = list(nums)
    nums[0] = 0
    for i in nums:
        sum += i
    return sum

print(add(2, 3, 7, 4))