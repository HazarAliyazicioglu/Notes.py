# set = Verilerin belirli bir sırası yada dizilimi olmayan koleksiyonlardır. Aynı veri tekrar edemez

food = {"hamburger", "lahmacun", "pizza"}
dessert = {"pudding", "ekler", "ice cream"}


food.add("güveç")
food.remove("pizza")
# food.clear()
food.update(dessert)                # Eğer başka bir set ismi yazılırsa yazılan setteki veriler içeri aktarılır. Eğer string bir ifade kullanılırsa harfler teker teker içeri aktarılır
dinner_table = food.union(dessert)  # Birden fazla set kullanarak yeni bir set oluşturur
print(dessert.difference(food))     # Bir setin diğerinden farklı olan elemenlarını seçer
print(food.intersection(dessert))   # Bir setle diğer set/setler arasındaki ortak elemanı seçer

for x in dinner_table:
    print(x)

