# Чтение первого списка
n1 = int(input("Количество чисел в первом списке: "))
list1 = []
for i in range(n1):
   list1.append(int(input()))

# Чтение второго списка  
n2 = int(input("Количество чисел во втором списке: "))
list2 = []
for i in range(n2):
   list2.append(int(input()))

# Преобразуем в множества и находим пересечение
set1 = set(list1)
set2 = set(list2)
common_elements = set1.intersection(set2)

# Выводим количество общих элементов
print(f"Количество общих чисел: {len(common_elements)}")