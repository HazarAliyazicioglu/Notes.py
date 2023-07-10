# sort() method = Listelerde kullanılır
# sort() function = İterablelerle kullanılır ( İterable = bir for döngüsü yardımıyla döngülenebilen veya yinelenebilen bir nesnedir. Lİsteler, setler, tupleler )

# sort() methodu (Sadece listelerde kullanılır)
students = ["Squidward", "Spongebob", "Sandy", "Patrick", "Mr.Krabs"]
students.sort(reverse=True)  # Tersine düzenler
for i in students:
    print(i)
print()

# sort() fonksiyonu (liste ,set, tuple gibi nesnelerde kullanılabilir)
sorted_students = sorted(students, reverse=True)
for i in sorted_students:
    print(i)
print()

student_grades = [("Squidward", "F", 60), ("Spongebob", "A", 33), ("Sandy", "D", 36), ("Patrick", "B", 20), ("Mr.Krabs", "C", 78)]
grade = lambda grades: grades[1]
sorted_grades = sorted(student_grades, key=grade)
for i in sorted_grades:
    print(i)
print()

age = lambda ages: ages[2]
sorted_grades = sorted(student_grades, key=age, reverse=True)
for i in sorted_grades:
    print(i)